from src.services.provider.provider import send_message
from src.models.message import Message
from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session 
from src.models.message import Message
from src.models.conversation import Conversation
from src.models.model import Model
from src.schemas.chat import ChatRequest,ChatResponse
from uuid import uuid4
from src.schemas.chat import ConversationRespone
from src.schemas.model import ModelResponse


def create_conversation(session: Session):
    id = uuid4()
    created_at = datetime.now()
    conversation = Conversation(
        id=id,
        created_at = created_at
    )
    session.add(conversation)
    session.commit()
    session.refresh(conversation)
    return conversation

def create_model(session : Session , model_name : str):
    id = uuid4()
    model = Model(
        id = id ,
        name = model_name
    )
    session.add(model)
    session.commit()
    session.refresh(model)
    return model


def load_models(session : Session):
    stmt = session.query(Model)
    models = session.scalars(stmt).all()
    return [ModelResponse.model_validate(model) for model in models]


def load_conversation(session:Session):
    stmt = session.query(Conversation)
    conversations = session.scalars(stmt).all()
    return [ConversationRespone.model_validate(conversation) for conversation in conversations]


def load_messages(session: Session , conversation_id : str):
    stmt = session.query(Message).where(Message.conversation_id == conversation_id )
    messages= session.scalars(stmt).all()
    return [ChatResponse.model_validate(message) for message in messages]


def create_message(session : Session , chat_request : ChatRequest ):
    id = uuid4()
    conversation_id = chat_request.conversation_id
    content = chat_request.content
    role = chat_request.role
    created_at = datetime.now()
    message = Message(
        id=id,
        conversation_id = conversation_id,
        content = content,
        role = role,
        created_at = created_at
    )

    session.add(message)
    session.commit()
    session.refresh(message)
    return message


def chat_model( session : Session , chat_request : ChatRequest ):
    create_message(session=session , chat_request=chat_request)
    conversation = load_messages(session=session , conversation_id=chat_request.conversation_id)
    response = send_message(conversation, chat_request.model)
    chatrequest = ChatRequest(
        conversation_id= chat_request.conversation_id,
        role='assistant',
        content = response,
        model = chat_request.model
    )

    message = create_message(session= session, chat_request=chatrequest)
    return message
