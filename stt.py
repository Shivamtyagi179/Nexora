from faster_whisper import WhisperModel

# small model fast hota hai
model = WhisperModel("base", compute_type="int8")


def transcribe(audio_path):

    segments, info = model.transcribe(str(audio_path))

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()