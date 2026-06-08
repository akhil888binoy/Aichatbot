from pydantic import BaseModel
from pydantic import BaseModel, Field , ConfigDict


class ModelResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : str 
    name: str 