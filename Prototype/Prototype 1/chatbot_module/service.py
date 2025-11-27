import ollama
from .prompts import INSIGHT_SPHERE_SYSTEM_PROMPT

class OllamaService:
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.system_prompt = INSIGHT_SPHERE_SYSTEM_PROMPT

    def generate_response(self, user_message: str, stream: bool = False):
        """
        Generates a response from the Ollama model.
        If stream is True, yields chunks of the response.
        """
        try:
            response = ollama.chat(model=self.model, messages=[
                {
                    'role': 'system',
                    'content': self.system_prompt,
                },
                {
                    'role': 'user',
                    'content': user_message,
                },
            ], stream=stream)

            if stream:
                for chunk in response:
                    yield chunk['message']['content']
            else:
                return response['message']['content']
        except Exception as e:
            if stream:
                yield f"Error communicating with Ollama: {str(e)}"
            else:
                return f"Error communicating with Ollama: {str(e)}"
