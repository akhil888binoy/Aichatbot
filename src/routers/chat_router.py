from typing import List
from src.services import chat_service
from src.schemas.chat  import ChatRequest, ChatResponse, ConversationRespone
from src.schemas.model import ModelResponse
from src.database.database import get_session
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException


chat_router = APIRouter(
    prefix="/api/chats",
    tags =["chats"]
)

@chat_router.get("/conversation" , response_model=List[ConversationRespone])
def get_conversation(session : Session = Depends(get_session)):
    return chat_service.load_conversation(session=session)

@chat_router.get("/messages/:{conversation_id}", response_model=List[ChatResponse])
def get_messages(conversation_id : str , session : Session=Depends(get_session)):
    return chat_service.load_messages(session=session , conversation_id=conversation_id)

@chat_router.get("/model " , response_model=List[ModelResponse])
def get_models(session : Session = Depends(get_session)):
    return chat_service.load_models(session=session)

@chat_router.post("/chat" , response_model=ChatResponse , status_code=201)
def chat_model(chat_request: ChatRequest , session : Session = Depends(get_session)):
    return chat_service.chat_model(session=session, chat_request=chat_request)