# AI-Powered NPC Generator for Games

## **Overview**
The AI-Powered NPC Generator API is designed to create detailed and dynamic non-playable characters (NPCs) for video games. It leverages predefined logic and optional AI to generate unique NPCs with attributes like names, roles, appearances, and backstories, making it a valuable tool for game developers.

## **Features**
- **Dynamic NPC Generation**: Generate NPCs with customizable attributes like species, profession, and traits.
- **AI-Enhanced Attributes**: Use AI or procedural rules to create imaginative backstories and personalities.
- **Storage & Retrieval**: Save generated NPCs to a database and retrieve them based on filters like role or personality.
- **Export Options**: Export NPC details in JSON, YAML, or other formats.
- **Interactive API**: Easily integrate with games using RESTful endpoints.

### **Key Components**
1. **`main.py`**: The entry point for the FastAPI application.
2. **`config.py`**: Application configuration (e.g., database URL).
3. **`database.py`**: Database connection initialization using SQLAlchemy.
4. **`models/npc.py`**: SQLAlchemy model for NPCs.
5. **`schemas/npc.py`**: Pydantic schemas for request validation and response.
6. **`routers/npc.py`**: API endpoints for NPC management.
7. **`services/npc_service.py`**: Business logic for generating and managing NPCs.
8. **`utils/ai_generator.py`**: Logic for generating NPC attributes, optionally enhanced by AI.

## **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nikosane/ai-npc-generator.git
   cd ai-npc-generator
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file and configure the database URL:
     ```env
     DATABASE_URL=sqlite:///./npc_database.db
     ```

5. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

## **Endpoints**
### **NPC Routes**
- **Generate NPC**: `POST /npc/`
  - Request: Specify optional attributes like role or traits.
  - Response: Returns a generated NPC with attributes.

- **Retrieve NPCs**: `GET /npc/`
  - Response: List all stored NPCs.

- **Retrieve NPC by ID**: `GET /npc/{id}`
  - Response: Returns details of a specific NPC.

- **Export NPC**: `GET /npc/{id}/export`
  - Response: Returns the NPC data in a specified format (JSON, YAML, etc.).

## **Technologies Used**
- **FastAPI**: Framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Database for local development.
- **Pydantic**: Data validation and parsing.
- **Optional AI Integration**: Add AI-based NPC generation with custom logic.


## **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests.

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

