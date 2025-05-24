import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class GeminiAPIError(Exception):
    pass

class GeminiClient:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise GeminiAPIError("Gemini API key is not set in environment variables.")
        genai.configure(api_key=GEMINI_API_KEY)
        try:
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        except Exception as e:
            raise GeminiAPIError(f"Failed to initialize Gemini model: {str(e)}")

    async def generate_response(self, prompt: str, temperature=0.5, max_tokens=256) -> str:
        try:
            
            import asyncio
            loop = asyncio.get_running_loop()
            response = await loop.run_in_executor(
                None,
                lambda: self.model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "max_output_tokens": max_tokens,
                    }
                )
            )
            return response.text.strip()
        except Exception as e:
            raise GeminiAPIError(f"Error while generating response: {str(e)}")
