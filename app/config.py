from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./npc_database.db")
