from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    
    id: Optional[int] = None
    ci: str 
    name: str
    last_name: str
    user_name: str
    password: str 
    email: str 
    adress: str 
    phone: str 
    date_create: str
    date_update: str 
    status = bool
    
    
    
    
    
    