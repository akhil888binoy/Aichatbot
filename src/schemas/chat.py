from typing import Optional
import datetime
from pydantic import BaseModel, ConfigDict, Field

class ChatRequest(BaseModel):
    conversation_id : str = Field(min_length=1,max_length=50)
    role : str = Field(min_length=1,max_length=50)
    content : str = Field(min_length=1,max_length=50)
    model : str = Field(min_length=1,max_length=50)

class ChatResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int  
    conversation_id : str 
    created_at : datetime.datetime  
    role : str  
    content : str  

class ConversationRespone(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : str
    created_at : datetime.datetime