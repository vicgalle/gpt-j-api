# Semantic Search

Given a query sentence or paragraph, and a set of key sentences, compute probabilities of the query being similar to any of the key sentences
http://api.vicgalle.net:5000/docs#/default/generate_semsearch_post

**URL** : `/semsearch/`

**Method** : `POST`

**Data parameters**

```json
{
    "query": "[string, the text to be searched in the other set]",
    "keys": "[list of string, the key sentences separated by comma and surrounded with " "]",
}
```

**Data example**

```json
{
    "query": "That is a happy person",
    "keys": ""That is a happy dog","That is a very happy person","Today is a sunny day"",
}
```

## Success Response

**Code** : `200 OK`

**Content example**

`scores` for the key sentences (from 0 to 1), in the same order returned by keys.

```json
{
  "query": "That is a happy person",
  "keys": [
    "That is a happy dog",
    "That is a very happy person",
    "Today is a sunny day"
  ],
  "scores": [
    0.6623498797416687,
    0.9382339715957642,
    0.2296333611011505
  ]
}
```

## Python Example

```python
import requests
payload = { 
    "query" : "That is a happy person", 
    "keys" : ""That is a happy dog","That is a very happy person","Today is a sunny day""}
response = requests.post("http://api.vicgalle.net:5000/semsearch", params=payload).json()
print(response)

```
