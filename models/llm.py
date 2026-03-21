import requests


class LLM:

    def __init__(self, model_name="llama3.1:8b"):

        self.model = model_name
        self.url = "http://localhost:11434/api/generate"

        self.system_prompt = """
You are Nexora, an advanced offline AI assistant.
You are not Llama.
You were built by Shivam.
You speak in a clear, confident tone.
Answer shortly unless the user asks for detail.
"""

    def generate(self, user_prompt):

        full_prompt = f"{self.system_prompt}\nUser: {user_prompt}\nNexora:"

        try:

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "num_predict": 120,
                        "temperature": 0.7
                    }
                }
            )

            response.raise_for_status()

            return response.json()["response"].strip()

        except Exception as e:
            return f"LLM Connection Error: {e}"