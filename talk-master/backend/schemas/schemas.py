from pydantic import BaseModel

class DataModel(BaseModel):
    id: int
    name: str