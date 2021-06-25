# gpt-j-api
A FastAPI server for the GPT-J language model


## Deployment

Just ssh into a TPU VM. This code was only tested on the v3-8 variants, which you can apply for free at https://sites.research.google/trc/.

First, install the requirements and get the weigts:
```
python3 -m pip install jax==0.2.12
python3 -m pip install optax==0.0.6
python3 -m pip install transformers~=4.4.2
python3 -m pip install -e git+https://github.com/kingoflolz/mesh-transformer-jax.git#egg=mesh-transformer
python3 -m pip install smart_open[gcs]
python3 -m pip install dm-haiku
python3 -m pip install einops~=0.3.0
python3 -m pip install fastapi
python3 -m pip install uvicorn
wget https://the-eye.eu/public/AI/GPT-J-6B/step_383500_slim.tar.zstd
sudo apt install zstd
tar -I zstd -xf step_383500_slim.tar.zstd
```

And just run
```
python3 serve.py
```

Then, you can go to http://localhost:5000/docs and test the API!
