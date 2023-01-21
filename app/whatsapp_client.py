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

        print(response)
        
        assert response.status_code == 200, "Error sending message"

        return response.status_code

    def send(self, token, to, template_name, language_code):
        url = 'https://graph.facebook.com/v15.0/111679144885464/messages'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            "messaging_product": 'whatsapp',
            "to": to,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }
        response = requests.post(url, json=data, headers=headers)
        
        print("\n" + str(response.json()))

        assert response.status_code == 200, "Error sending message"

        return response.status_code


    def process_webhook_notification(self, data):
        """_summary_: Process webhook notification
        For the moment, this will return the type of notification
        """

        response = []

        for entry in data["entry"]:

            for change in entry["changes"]:
                response.append(
                    {
                        "type": change["field"],
                        "from": change["value"]["metadata"]["display_phone_number"],
                    }
                )

        return response


if __name__ == "__main__":
    client = WhatsAppWrapper()
    client.send_template_message("hello_world", "en_US", os.environ.get("WHATSAPP_NUMBER_WEBHOOK_TEST"))
    