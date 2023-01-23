import os
import openai
# from dotenv import load_dotenv

import json

# load_dotenv()

class OpenAIWrapper:
    def __init__(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        print ("\nopenai key is" + openai.api_key + " and its type is " + openai.api_type)

    def complete(self, prompt):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        print ("response form openai is :\n" + str(response) + "\n")
        return response.choices[0].text

if __name__ == "__main__":
    client = OpenAIWrapper()
    response = client.complete("how are you")
    print (response)
    