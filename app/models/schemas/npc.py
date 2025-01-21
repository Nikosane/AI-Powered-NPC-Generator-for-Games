from pydantic import BaseModel

class NPCBase(BaseModel):
    name: str
    role: str
    backstory: str

class NPCCreate(NPCBase):
    pass

class NPCResponse(NPCBase):
    id: int

    class Config:
        orm_mode = True
