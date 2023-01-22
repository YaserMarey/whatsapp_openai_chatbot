import os
import requests
import openai

import json


class OpenAIWrapper:

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    def __init__(self):
        pass

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
    