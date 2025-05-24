from app.tools.calculator import CalculatorTool
from app.utils.gemini_client import GeminiClient, GeminiAPIError
from app.utils.error_handlers import AgentError
import re
import asyncio
from typing import Optional

class MathAgent:
    def __init__(self):
        self.calculator = CalculatorTool()
        self.gemini = GeminiClient()

    async def handle_query(self, query: str) -> str:
        
        expr = self.extract_expression(query)
        if expr:
            result = self.calculator.evaluate_expression(expr)
            if "Error" not in result and "Invalid" not in result:
                return f"The result of the calculation `{expr}` is: {result}"

        
        prompt = f"You are a math expert. Answer this question clearly and concisely:\n{query}"
        try:
            answer = await self.gemini.generate_response(prompt)
            return answer
        except GeminiAPIError as e:
            raise AgentError(f"Math Agent failed: {str(e)}")

    

    def extract_expression(self, query: str) -> Optional[str]:
        """
        Extract arithmetic expression from the query, e.g. "solve 2x + 5 = 11"
        We'll only support simple expressions containing digits and operators.
        """
        # A naive regex to extract expressions with digits and operators
        match = re.search(r"([\d+\-*/().\s]+)", query)
        if match:
            expr = match.group(1).strip()
            # Reject empty or very short matches
            if len(expr) > 1:
                return expr
        return None
