from models.llm import ask_llm
from models.tts import speak

def process_text(user_text):

    reply = ask_llm(user_text)

    print("Nexora:", reply)

    speak(reply)

    return reply