import os
from fastapi import FastAPI
from src.routers.chat_router import chat_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(debug=os.getenv("DEBUG", "False").lower() == "true")
app.include_router(chat_router)
