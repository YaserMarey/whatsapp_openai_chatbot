from whatsapp_openai_chatbot.app.webhook import app
import uvicorn 
if __name__ == "__main__":
    uvicorn.run("app.webhook:app", port=5000, log_level="info")