from app.main import app
import uvicorn 
if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8000, log_level="info")