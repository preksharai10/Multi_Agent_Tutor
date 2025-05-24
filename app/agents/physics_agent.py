from app.tools.constants import lookup_constant
from app.utils.gemini_client import GeminiClient, GeminiAPIError
from app.utils.error_handlers import AgentError
import re
import asyncio
from typing import Optional

class PhysicsAgent:
    def __init__(self):
        self.gemini = GeminiClient()

    async def handle_query(self, query: str) -> str:
        
        const_name = self.extract_constant_name(query)
        if const_name:
            const_value = lookup_constant(const_name)
            return f"{const_name.capitalize()}: {const_value}"

        
        prompt = f"You are a physics expert. Provide a clear answer to the following question:\n{query}"
        try:
            answer = await self.gemini.generate_response(prompt)
            return answer
        except GeminiAPIError as e:
            raise AgentError(f"Physics Agent failed: {str(e)}")
    def extract_constant_name(self, query: str) -> Optional[str]:
        """
        Checks if query mentions a known constant and returns its name
        """
        constants = [
            "speed of light",
            "gravitational constant",
            "planck constant",
            "electron mass",
            "proton mass"
        ]
        for const in constants:
            if const in query.lower():
                return const
        return None
        return None
