# An implementation of a WhatsApp OpenAI Chatbot using WhatsApp Cloud API and Webhooks with FastAPI 

## Installation

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

And then run the server:

```shell
flask run
```