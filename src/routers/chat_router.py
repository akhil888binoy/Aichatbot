from typing import List
from src.services import chat_service
from src.schemas.chat  import ChatRequest, ChatResponse, ConversationRespone
from src.schemas.model import ModelResponse,ModelRequest
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

@chat_router.get("/messages/{conversation_id}", response_model=List[ChatResponse])
def get_messages(conversation_id : str , session : Session=Depends(get_session)):
    return chat_service.load_messages(session=session , conversation_id=conversation_id)

@chat_router.get("/model" , response_model=List[ModelResponse])
def get_models(session : Session = Depends(get_session)):
    return chat_service.load_models(session=session)

@chat_router.post("/create_conversation", response_model= ConversationRespone , status_code=201)
def create_conversation(session : Session = Depends(get_session)):
    return chat_service.create_conversation(session=session)

@chat_router.post("/chat" , response_model= ChatResponse , status_code=201)
def chat_model(chat_request: ChatRequest , session : Session = Depends(get_session)):
    response = chat_service.chat_model(session=session, chat_request=chat_request)
    chat_response = ChatResponse(
        id = response.id,
        conversation_id=response.conversation_id,
        created_at= response.created_at,
        role = response.role,
        content=response.content
    )
    return chat_response

@chat_router.post('/create_model', response_model= ModelResponse , status_code=201)
def create_model(model_request: ModelRequest , session : Session = Depends(get_session)):
    return chat_service.create_model(session=session , model_name=model_request.name)