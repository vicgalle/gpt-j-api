# Generate

Given a prompt, generate some text using the GPT-J language model
http://api.vicgalle.net:5000/docs#/default/generate_generate_post

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
    "context": "In a shocking finding, scientists discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.",
    "token_max_length": 512,
    "temperature": 1.0,
    "top_p": 0.9,
    "stop_sequence": ""
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "model": "GPT-J-6B",
  "compute_time": 8.957557201385498,
  "text": "\n\nThe Unicorns spoke English\n\nThe valley, located in the middle of the Urubamba river, is full of vineyards and greenery, yet it’s been uninhabited for the past 30 years. After this isolation, the valley became a great environment for dinosaurs to flourish, particularly birds and tyrannosaurs. The valley has been preserved this way since the dinosaurs became extinct.\n\nThe scientists also found that the unicorns were very good at video gaming, thus, there was a large population of high-level players of a popular video game. Even more amazing is the fact that the unicorns spoke perfect English. The unicorns also possessed all of the skills and attributes that humans possess, which included self-control, coordination, self-confidence, self-awareness, kindness, empathy, and honesty. It was even revealed that these unicorns were also aware of the consequences of their actions and did not commit illegal acts. These unicorns didn’t try to hurt others or did not steal from them.\n\nThese unicorns were smart, patient, and full of morality\n\nThe unicorns didn’t commit any crimes in their environment, but they didn’t get mad at one another either. Whenever someone acted in an unkind manner, the unicorns merely tried to make them happy, rather than acting violent against them. The scientists also reported that the unicorns were actually curious, and they got the most pleasure out of exploring new surroundings. However, even with these attributes, the unicorns did not intend to harm others.\n\nIt was also discovered that the unicorns practiced altruism, which is the act of one party providing something to another party who is not involved. It was also revealed that the unicorns don’t just have all of these attributes. These unicorns were even capable of feelings such as anger, jealousy, and hate. However, the unicorns seemed to not have much of these qualities. The unicorns were very laid back, relaxed, and even tranquil. They felt that they could relate to other animals much better than humans could.\n\nThe unicorns suffered and witnessed more violence in the past\n\nDespite being protected by the law and technology, the unicorns still lost many family members and they suffered much violence and threats. The unicorns were then forced to move from their valley. These unicorns didn’t even have an opportunity to grow up, as they were separated from their families very early on. With such a high",
  "prompt": "In a shocking finding, scientists discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.",
  "token_max_length": 512,
  "temperature": 1,
  "top_p": 0.9,
  "stop_sequence": null
}
```

## Python Example

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
