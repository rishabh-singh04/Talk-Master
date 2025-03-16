# text_to_speech.py
from gtts import gTTS
import os

def text_to_speech(text, temp_dir):
    """Convert text to speech and save as an audio file."""
    tts = gTTS(text)
    file_path = os.path.join(temp_dir, "output.mp3")
    tts.save(file_path)
    return file_path