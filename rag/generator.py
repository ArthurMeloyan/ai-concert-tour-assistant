import google.generativeai as genai
from config import GEMINI_API_KEY, GENERATION_MODEL

genai.configure(api_key=GEMINI_API_KEY)

_model = None


def _get_model():
    global _model
    if _model is None:
        _model = genai.GenerativeModel(
            model_name=GENERATION_MODEL,
            system_instruction="You are a helpful assistant for answering questions about concert tours.",
        )
    return _model


def generate_answer(prompt: str) -> str:
    try:
        response = _get_model().generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error during generation: {str(e)}"
