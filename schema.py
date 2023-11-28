from pydantic import BaseModel

class Plants_post(BaseModel):
    name: str
    description: str
    family_id: int

class Family(BaseModel):
    name: str
    description: str

class Seed(BaseModel):
    name: str
    description: str
    plant_id: int

