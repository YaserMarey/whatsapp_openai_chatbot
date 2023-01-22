import os
import requests
import openai
from dotenv import load_dotenv

import json

load_dotenv()

class OpenAIWrapper:
    def __init__(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def complete(self, prompt):

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.0,
        )
        return response.choices[0].text

if __name__ == "__main__":
    client = OpenAIWrapper()
    response = client.complete("hello")
    print (response)
    