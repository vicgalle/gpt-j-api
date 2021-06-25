# gpt-j-api
A FastAPI server for the GPT-J language model. You can test and use the API at http://34.90.255.118:5000/docs


## Deployment

Just ssh into a TPU VM. This code was only tested on the v3-8 variants, which you can apply for free at https://sites.research.google/trc/.

First, install the requirements and get the weigts:
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
