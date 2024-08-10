
Focusing solely on the cURL, HTTP request, and Python examples while keeping the rest of the documentation intact without modification:

# Translate Text

API reference for translating text with the DeepL API.

## Endpoint

`POST https://api.deepl.com/v2/translate`

## Headers

- `Authorization`: `DeepL-Auth-Key [yourAuthKey]`
- `Content-Type`: `application/json`

## Request Body Parameters

```json
{
  "text": [
    "Hello, world!"
  ],
  "target_lang": "DE"
}
```

## Example Request (cURL)

```bash
curl -X POST 'https://api.deepl.com/v2/translate' \
--header 'Authorization: DeepL-Auth-Key [yourAuthKey]' \
--header 'Content-Type: application/json' \
--data '{
  "text": [
    "Hello, world!"
  ],
  "target_lang": "DE"
}'
```

## Python Example

```python
import deepl

auth_key = "f63c02c5-f056-..."  # Replace with your key
translator = deepl.Translator(auth_key)
result = translator.translate_text("Hello, world!", target_lang="FR")
print(result.text)  # "Bonjour, le monde !"
```

## HTTP Request

```
POST /v2/translate HTTP/2
Host: api.deepl.com
Authorization: DeepL-Auth-Key [yourAuthKey]
Content-Type: application/json

{
  "text": ["Hello, world!"],
  "target_lang": "DE"
}
```

## Response

```json
{
  "translations": [
    {
      "detected_source_language": "EN",
      "text": "Hallo, Welt!"
    }
  ]
}
```

---

This streamlined documentation focuses on cURL, HTTP request, and Python examples for making translation requests to the DeepL API, omitting other languages and unnecessary details.
