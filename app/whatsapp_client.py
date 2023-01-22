import os
import requests

import json


class WhatsAppWrapper:

    API_URL = "https://graph.facebook.com/v15.0/"
    API_TOKEN = os.environ.get("WHATSAPP_API_TOKEN")
    NUMBER_ID = os.environ.get("WHATSAPP_NUMBER_ID")

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}",
            "Content-Type": "application/json",
        }
        self.API_URL = self.API_URL + self.NUMBER_ID

    def send_template_message(self, template_name, language_code, phone_number):

        payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }

        response = requests.post(f"{self.API_URL}/messages", json=payload,headers=self.headers)

        assert response.status_code == 200, "Error sending message"

        return response.status_code


    def send_text_message(self,to, message):
        payload = {
            "messaging_product": 'whatsapp',
            "to": to,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message
            }
        }
        response = requests.post(f"{self.API_URL}/messages", json=payload,headers=self.headers)
        assert response.status_code == 200, "Error sending message"
        return response.status_code


    def process_webhook_notification(self, data):
        """_summary_: Process webhook notification
        For the moment, this will return the type of notification
        """
        entries = data["entry"]
        for entry in entries:
            for change in entry["changes"]:
                value = change["value"]
                if value:
                    phone_number_id = value["metadata"]["phone_number_id"]
                    if "messages" in value:
                        for message in value["messages"]:
                            if message["type"] == "text":
                                from_ = message["from"]
                                message_body = message["text"]["body"]
                                reply_message = f"Ack from FastAPI-WtsApp Webhook: {message_body}"
                                
                                client.send_text_message(phone_number_id, reply_message)
                                return {
                                    "statusCode": 200,
                                    "body": json.dumps("Done"),
                                    "isBase64Encoded": False
                                }

        return {
            "statusCode": 403,
            "body": json.dumps("Unsupported method"),
            "isBase64Encoded": False
        }


if __name__ == "__main__":
    client = WhatsAppWrapper()
    client.send_template_message("hello_world", "en_US", os.environ.get("WHATSAPP_NUMBER_WEBHOOK_TEST"))
    