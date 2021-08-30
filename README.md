# gpt-j-api 🦜
![GitHub release (latest by date)](https://img.shields.io/github/v/release/vicgalle/gpt-j-api?color=blueviolet)
![Python version](https://img.shields.io/badge/python-3.7-blueviolet)
![API up](https://github.com/vicgalle/gpt-j-api/actions/workflows/test.yml/badge.svg)


An API to interact with the GPT-J language model and variants! You can use and test the model in two different ways:

* Streamlit web app at http://api.vicgalle.net:8000/ 
* The proper API, documented at http://api.vicgalle.net:5000/docs

## Open API endpoints 🔓

These are the endpoints of the public API and require no authentication.
Click on each to see the parameters!

#### GPT-J text generation 🤖

* [generate](docs/generate.md) : `POST /generate/`

#### Zero-shot text classification (multilingual) 🌍

* [classify](docs/classify.md) : `POST /classify/`

## Using the API 🔥

* Python:

```python
import requests
context = "In a shocking finding, scientist discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English."
payload = {
    "context": context,
    "token_max_length": 512,
    "temperature": 1.0,
    "top_p": 0.9,
}
response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()
print(response)
```

* Python (zero-shot classification):

```python
import requests
payload = { 
    "sequence" : "The movie started slow, but in the end was absolutely amazing!", 
    "labels" : "positive,neutral,negative"}
response = requests.post("http://api.vicgalle.net:5000/classify", params=payload).json()
print(response)
```

* Bash:

```bash
curl -X 'POST' \
  'http://api.vicgalle.net:5000/generate?context=In%20a%20shocking%20finding%2C%20scientists%20discovered%20a%20herd%20of%20unicorns%20living%20in%20a%20remote%2C%20previously%20unexplored%20valley%2C%20in%20the%20Andes%20Mountains.%20Even%20more%20surprising%20to%20the%20researchers%20was%20the%20fact%20that%20the%20unicorns%20spoke%20perfect%20English.&token_max_length=512&temperature=1&top_p=0.9' \
  -H 'accept: application/json' \
  -d ''
```

## Deployment of the API server

Just ssh into a TPU VM. This code was only tested on the v3-8 variants.

First, install the requirements and get the weights:
```
python3 -m pip install -r requirements.txt
wget https://the-eye.eu/public/AI/GPT-J-6B/step_383500_slim.tar.zstd
sudo apt install zstd
tar -I zstd -xf step_383500_slim.tar.zstd
```

And just run
```
python3 serve.py
```

Then, you can go to http://localhost:5000/docs and use the API!

## Deploy the streamlit dashboard

Just run

```
python3 -m streamlit run streamlit_app.py --server.port 8000
```


## Acknowledgements

Thanks to the support of the TPU Research Cloud, https://sites.research.google/trc/
