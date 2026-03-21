from models.llm import LLM
from models.tts import speak
from audio.player import play_audio

# ✅ only STT (Vosk)
from models.stt import transcribe


def main():

    print("🤖 Nexora Voice Assistant Started")
    print("🎤 Speak to interact | say 'exit' to quit\n")

    llm = LLM()

    # 🔊 startup voice
    play_audio(speak("Hello, I am Nexora. Your AI assistant is ready."))

    while True:

        print("\n🎤 Listening... Speak now")

        # 🎤 Direct speech → text
        user_input = transcribe()

        print("🧑 You:", user_input)

        # ⚠️ empty input
        if not user_input:
            print("⚠️ Didn't catch that, try again...")
            continue

        # ❌ exit condition
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Exiting Nexora...")
            play_audio(speak("Goodbye. See you soon."))
            break

        # 🤖 LLM response
        response = llm.generate(user_input)

        if not response:
            print("⚠️ Nexora couldn't respond.")
            continue

        print("🤖 Nexora:", response)

        # 🔊 speak response
        play_audio(speak(response))


if __name__ == "__main__":
    main()