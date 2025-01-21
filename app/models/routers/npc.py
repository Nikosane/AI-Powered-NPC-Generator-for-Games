from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.npc import NPC
from app.schemas.npc import NPCCreate, NPCResponse

router = APIRouter(prefix="/npc", tags=["NPC"])

@router.post("/", response_model=NPCResponse)
def create_npc(npc: NPCCreate, db: Session = Depends(get_db)):
    new_npc = NPC(**npc.dict())
    db.add(new_npc)
    db.commit()
    db.refresh(new_npc)
    return new_npc

@router.get("/{npc_id}", response_model=NPCResponse)
def get_npc(npc_id: int, db: Session = Depends(get_db)):
    return db.query(NPC).filter(NPC.id == npc_id).first()
