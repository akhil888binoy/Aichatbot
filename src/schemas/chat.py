from typing import Optional
import datetime
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID

class ChatRequest(BaseModel):
    conversation_id : UUID 
    role : str = Field(min_length=1,max_length=5000)
    content : str = Field(min_length=1,max_length=5000)
    model : str = Field(min_length=1,max_length=5000)

class ChatResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : UUID  
    conversation_id : UUID 
    created_at : datetime.datetime  
    role : str  
    content : str  

class ConversationRespone(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : UUID
    created_at : datetime.datetime