import logging
from app.utils.gemini_client import GeminiClient


logger = logging.getLogger(__name__)

class ChemistryAgent:
    """
    Handles chemistry-related questions using Gemini.
    """

    async def handle_task(self, question: str) -> str:
        prompt = f"Answer this chemistry question clearly and accurately:\n{question}"
        try:
            response = await GeminiClient(prompt)
            return response
        except Exception as e:
            logger.error(f"ChemistryAgent failed: {e}")
            return "Sorry, I couldn't answer the chemistry question at the moment."
