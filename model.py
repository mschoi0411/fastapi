from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id : int
    author: str
    item: str
    timestamp : datetime
