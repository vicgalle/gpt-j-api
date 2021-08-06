import time

import jax
from jax.experimental import maps
import numpy as np
import optax
import transformers

from mesh_transformer.checkpoint import read_ckpt
from mesh_transformer.sampling import nucleaus_sample
from mesh_transformer.transformer_shard import CausalTransformer

from fastapi import FastAPI
import uvicorn

from typing import Optional

app = FastAPI()
params = {
    "layers": 28,
    "d_model": 4096,
    "n_heads": 16,
    "n_vocab": 50400,
    "norm": "layernorm",
    "pe": "rotary",
    "pe_rotary_dims": 64,
    "seq": 2048,
    "cores_per_replica": 8,
    "per_replica_batch": 1,
}

per_replica_batch = params["per_replica_batch"]
cores_per_replica = params["cores_per_replica"]
seq = params["seq"]


params["sampler"] = nucleaus_sample

# here we "remove" the optimizer parameters from the model (as we don't need them for inference)
params["optimizer"] = optax.scale(0)

mesh_shape = (jax.device_count() // cores_per_replica, cores_per_replica)
devices = np.array(jax.devices()).reshape(mesh_shape)

maps.thread_resources.env = maps.ResourceEnv(maps.Mesh(devices, ("dp", "mp")))

tokenizer = transformers.GPT2TokenizerFast.from_pretrained("gpt2")

total_batch = per_replica_batch * jax.device_count() // cores_per_replica

network = CausalTransformer(params)
network.state = read_ckpt(network.state, "./step_383500/", devices.shape[1])
del network.state["opt_state"]
network.state = network.move_xmap(network.state, np.zeros(cores_per_replica))


@app.post("/generate")
async def generate(
    context: Optional[
        str
    ] = "In a shocking finding, scientists discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.",
    token_max_length: Optional[int] = 512,
    temperature: Optional[float] = 1.0,
    top_p: Optional[float] = 0.9,
    stop_sequence: Optional[str] = None,
):
    start = time.time()
    tokens = tokenizer.encode(context)
    provided_ctx = len(tokens)
    if token_max_length + provided_ctx > 2048:
        return {"text": "Don't abuse the API, please."}
    pad_amount = seq - provided_ctx

    padded_tokens = np.pad(tokens, ((pad_amount, 0),)).astype(np.uint32)
    batched_tokens = np.array([padded_tokens] * total_batch)
    length = np.ones(total_batch, dtype=np.uint32) * len(tokens)

    output = network.generate(
        batched_tokens,
        length,
        token_max_length,
        {
            "top_p": np.ones(total_batch) * top_p,
            "temp": np.ones(total_batch) * temperature,
        },
    )

    text = tokenizer.decode(output[1][0][0, :, 0])

    # A simple technique to stop at stop_sequence without modifying the underlying model
    if stop_sequence is not None and stop_sequence in text:
        text = text.split(stop_sequence)[0] + stop_sequence

    response = {}
    response["model"] = "GPT-J-6B"
    response["compute_time"] = time.time() - start
    response["text"] = text
    response["prompt"] = context
    response["token_max_length"] = token_max_length
    response["temperature"] = temperature
    response["top_p"] = top_p
    response["stop_sequence"] = stop_sequence

    print(response)
    return response


print("GPT-J-6B serving!")
uvicorn.run(app, host="0.0.0.0", port=5000)
