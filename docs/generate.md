# Generate

Given a prompt, generate some text using the GPT-J language model


**URL** : `/generate/`

**Method** : `POST`

**Data parameters**

```json
{
    "context": "[string, the prompt to the model]",
    "token_max_length": "[int, the number of tokens to be generated]",
    "temperature": "[float, the temperature hyperparameter for the sampling]",
    "top_p": "[float, the top p sampling probability]",
    "stop_sequence": "[string, if present, when to stop the generation]"
}
```

**Data example**

```json
{
    "username": "iloveauth@example.com",
    "password": "abcd1234"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "token": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d"
}
```
