import os
import requests
import openai

import json


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
    