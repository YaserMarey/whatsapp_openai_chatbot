import os
from fastapi import FastAPI, Request, Response
from fastapi.encoders import jsonable_encoder

from app.whatsapp_client import WhatsAppWrapper
from app.openai_client import OpenAIWrapper

app = FastAPI()

VERIFY_TOKEN = os.environ.get("WHATSAPP_HOOK_TOKEN")

@app.get("/")
def hello_world():
    return "Hello World!!"

@app.get("/webhook/")
def subscribe(request: Request):
    if request.query_params.get('hub.verify_token') == VERIFY_TOKEN:
        return request.query_params.get('hub.challenge')
    return "Authentication failed. Invalid Token."

@app.post("/webhook/")
def process_notifications(request: Request):
    wtsapp_client = WhatsAppWrapper()
    print ("We received " + str(request))
    response = wtsapp_client.process_webhook_notification(request)
    if response["statusCode"] == 200:
        if response["body"] and response["from_no"]:
            openai_client = OpenAIWrapper()
            reply = openai_client.complete(prompt=response["body"])
            print ("\nreply is "  + reply)
            wtsapp_client.send_text_message(to=response["from_no"], message=reply)
            print ("We replied with " + str(response))

    return jsonable_encoder({"status": "success"}, 200)
