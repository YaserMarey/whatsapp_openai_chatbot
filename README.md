# An implementation of a WhatsApp OpenAI Chatbot using WhatsApp Cloud API and Webhooks with FastAPI 

## Installation

1- Create an account on Heroku
2- Push repo to Heroku
3- Create Facebook Developer Account 
4- Create Facebook App
5- Create Account on OpenAI
6- Set Environment Varialbes 
7- Test webhooks notification processing

## To test locally:

Make sure to have an `.env` file with the following variables:

```shell
WHATSAPP_API_TOKEN=
WHATSAPP_NUMBER_ID=
WHATSAPP_HOOK_TOKEN=
OPENAI_API_KEY=
```

Create virtual environment

```shell
python -m venv venv
./venv/bin/activate
```

And install the dependencies:

```shell
pip install install -r requirements.txt
``` 
