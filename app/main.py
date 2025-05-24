from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.agents.tutor_agent import TutorAgent
from app.utils.error_handlers import AgentError
import logging
import traceback

app = FastAPI(title="Multi-Agent Tutor")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Request model
class QueryRequest(BaseModel):
    question: str

# Initialize TutorAgent 
tutor_agent = TutorAgent()

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        logger.info(f"Received question: {request.question}")
        response = await tutor_agent.handle_query(request.question)
        logger.info(f"Response: {response}")
        
        return {"response": response}
    except AgentError as e:
        logger.error(f"AgentError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unhandled Exception: {e}\n{traceback.format_exc()}")
        
        raise HTTPException(status_code=500, detail="Internal server error")
