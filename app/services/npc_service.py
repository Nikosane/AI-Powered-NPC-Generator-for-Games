from sqlalchemy.orm import Session
from app.models.npc import NPC
from app.schemas.npc import NPCCreate

def create_npc_service(npc: NPCCreate, db: Session):
    new_npc = NPC(**npc.dict())
    db.add(new_npc)
    db.commit()
    db.refresh(new_npc)
    return new_npc

def get_npc_service(npc_id: int, db: Session):
    return db.query(NPC).filter(NPC.id == npc_id).first()
