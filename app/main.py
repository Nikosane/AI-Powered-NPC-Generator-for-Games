from fastapi import FastAPI
from app.routers import npc
from app.database import Base, engine

# Initialize database
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include NPC router
app.include_router(npc.router)

@app.get("/")
def root():
    return {"message": "Welcome to the AI-Powered NPC Generator API!"}
