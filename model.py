from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id : int
    item: str
    timestamp : datetime
