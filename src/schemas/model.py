from pydantic import BaseModel
from pydantic import BaseModel, Field , ConfigDict
import uuid

class ModelRequest(BaseModel):
    name : str
    
class ModelResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : uuid.UUID
    name: str 