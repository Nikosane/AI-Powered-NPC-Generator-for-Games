from sqlalchemy import Column, Integer, String
from app.database import Base

class NPC(Base):
    __tablename__ = "npcs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)
    backstory = Column(String)
