from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id : int
    name : str
    item: str
    timestamp : datetime
