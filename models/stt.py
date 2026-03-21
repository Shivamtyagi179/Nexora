import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

# 🎯 Model Path (IMPORTANT)
MODEL_PATH = "models/vosk-model"

# 🔄 Audio Queue
q = queue.Queue()


# 🎤 Mic Callback
def callback(indata, frames, time, status):
    if status:
        print("⚠️ Mic issue:", status)
    q.put(bytes(indata))


# 🧠 Speech to Text Function
def transcribe():
    try:
        print("🔄 Loading STT model...")
        model = Model(MODEL_PATH)

        recognizer = KaldiRecognizer(model, 16000)

        # 🎤 Start Listening
        with sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype='int16',
            channels=1,
            callback=callback
        ):
            print("🎤 Speak now...")

            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())

                    text = result.get("text", "").strip()

                    if text:
                        print("✅ Recognized:", text)
                        return text
                    else:
                        print("⚠️ No speech detected, try again...")
                        return ""

    except Exception as e:
        print("❌ STT Error:", e)
        return ""