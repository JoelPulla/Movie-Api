from sqlmodel import SQLModel, Field

class TvModel(SQLModel, table=True ):
    
    id:int | None = Field(default= None, primary_key= True)
    name:str = Field( min_length=3, max_length=20)
    description:str
    category:str
    languege:str
    url_streaming:str
    created_at:str
    
    