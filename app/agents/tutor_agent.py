from app.agents.math_agent import MathAgent
from app.agents.physics_agent import PhysicsAgent
from app.agents.chemistry_agent import ChemistryAgent
from app.utils.gemini_client import GeminiClient, GeminiAPIError
from app.utils.error_handlers import AgentError
import asyncio

class TutorAgent:
    def __init__(self):
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()
        self.chemistry_agent = ChemistryAgent()
        self.gemini = GeminiClient()

    async def classify_subject(self, question: str) -> str:
        """
        Use Gemini API or keyword matching to classify question subject.
        Returns one of: 'math', 'physics', 'chemistry', or 'general'.
        """
        keywords = {
            "math": ["solve", "calculate", "equation", "integrate", "derive", "algebra", "geometry"],
            "physics": ["force", "velocity", "gravity", "energy", "light", "mass", "acceleration", "newton"],
            "chemistry": ["atom", "molecule", "compound", "bond", "reaction", "chemical", "element", "acid", "base", "mol", "chemistry"]
        }

        question_lower = question.lower()
        for subject, kws in keywords.items():
            if any(kw in question_lower for kw in kws):
                return subject

        
        prompt = (
            "Classify the following question into one of these subjects: math, physics, chemistry, or general.\n"
            f"Question: {question}\nAnswer:"
        )
        try:
            classification = await self.gemini.generate_response(prompt)
            classification = classification.strip().lower()
            if classification in ["math", "physics", "chemistry", "general"]:
                return classification
            else:
                return "general"
        except GeminiAPIError:
            return "general"

    async def handle_query(self, question: str) -> str:
        subject = await self.classify_subject(question)

        if subject == "math":
            return await self.math_agent.handle_query(question)
        elif subject == "physics":
            return await self.physics_agent.handle_query(question)
        elif subject == "chemistry":
            return await self.chemistry_agent.handle_task(question)
        else:
            return "Sorry, I currently specialize in math, physics, and chemistry questions only."
