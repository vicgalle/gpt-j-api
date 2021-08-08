# Classify

Given a sentence or paragraph, and a set of labels, compute probabilities of the text being assigned to either label
http://api.vicgalle.net:5000/docs#/default/generate_classify_post

**URL** : `/classify/`

**Method** : `POST`

**Data parameters**

```json
{
    "sequence": "[string, the text to be classified]",
    "labels": "[string, the classes separated by comma]",
}
```

**Data example**

```json
{
    "sequence": "The movie started slow, but in the end was absolutely amazing!",
    "labels": "positive,neutral,negative",
}
```

## Success Response

**Code** : `200 OK`

**Content example**

`scores` are the probabilities for the labels, in the same order returned by labels.

```json
{
  "sequence": "The movie started slow, but in the end was absolutely amazing!",
  "labels": [
    "positive",
    "neutral",
    "negative"
  ],
  "scores": [
    0.9768275618553162,
    0.019993752241134644,
    0.0031787161715328693
  ]
}
```

## Python Example

```python
import requests
context = "In a shocking finding, scientist discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English."
payload = { 
    "sequence" : "The movie started slow, but in the end was absolutely amazing!", 
    "labels" : "positive,neutral,negative"}
response = requests.post("http://api.vicgalle.net:5000/classify", params=payload).json()
print(response)

```
