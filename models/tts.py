import subprocess
from pathlib import Path
import uuid

BASE_DIR = Path(__file__).resolve().parent.parent

PIPER = BASE_DIR / "piper" / "piper.exe"
MODEL = BASE_DIR / "piper" / "en_US-lessac-medium.onnx"
AUDIO_DIR = BASE_DIR / "audio"


def speak(text, lang="en"):

    output_file = AUDIO_DIR / f"output_{uuid.uuid4().hex}.wav"

    process = subprocess.Popen(
        [str(PIPER), "-m", str(MODEL), "-f", str(output_file)],
        stdin=subprocess.PIPE,
        text=True
    )

    process.communicate(text)

    return output_file