from pydantic import BaseModel, Field
from typing import Optional

class TvSchema(BaseModel, ):
    
    id:Optional[int] = Field(None)
    name:str
    description:str
    category:str
    languege:str
    url_streaming:str
    created_at:str