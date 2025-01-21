from fastapi import APIRouter
from .npc import router as npc_router

router = APIRouter()
router.include_router(npc_router)
