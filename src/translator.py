# src/translator.py

import httpx
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DeePLTranslator:
    def __init__(self):
        self.auth_key = os.getenv("DEEPL_API_KEY")
        self.base_url = "http://127.0.0.1:1188/v2/translate"
        self.client = httpx.Client()

    def translate_text(self, text, target_lang, source_lang='EN'):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"DeepL-Auth-Key {self.auth_key}"
        }

        data = {
            "text": [text],
            "target_lang": target_lang,
            "source_lang": source_lang
        }

        post_data = json.dumps(data)
        response = httpx.post(
            url=self.base_url, data=post_data, headers=headers)

        if response.status_code == 200:
            return response.json()["translations"][0]["text"]
        else:
            raise Exception(f"Failed to translate text: {response.text}")


# Example usage
if __name__ == "__main__":
    # Replace YOUR_AUTH_KEY_HERE with your actual auth key
    auth_key = "YOUR_AUTH_KEY_HERE"
    translator = DeePLTranslator(auth_key)
    translated_text = translator.translate_text("Hello, world!", "DE")
    print(translated_text)
