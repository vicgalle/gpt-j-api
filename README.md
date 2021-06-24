# gpt-j-api
A FastAPI server for the GPT-J language model


## Deployment

Just ssh into a TPU VM. This code was only tested on the v3-8 variants, which you can apply for free at https://sites.research.google/trc/.

```
python3 -m pip install -r requirements.txt
wget https://the-eye.eu/public/AI/GPT-J-6B/step_383500_slim.tar.zstd
sudo apt install zstd
tar -I zstd -xf step_383500_slim.tar.zstd
python3 serve.py
```
