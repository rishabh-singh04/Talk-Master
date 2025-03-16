from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import pytesseract
from pdf2image import convert_from_bytes
from gtts import gTTS
from PIL import Image
import os
import uuid
import tempfile

# Set up FastAPI
app = FastAPI()

# Set Tesseract-OCR installation path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Directory for saving audio files
TEMP_AUDIO_DIR = tempfile.gettempdir()

# Function to extract text from an image
def extract_text_from_image(image_bytes):
    image = Image.open(image_bytes)
    text = pytesseract.image_to_string(image)
    return text.strip()

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_bytes):
    images = convert_from_bytes(pdf_bytes)
    text = "\n".join(pytesseract.image_to_string(img) for img in images)
    return text.strip()

# Function to convert text to speech
def text_to_speech(text):
    if not text:
        raise HTTPException(status_code=400, detail="No text found to convert to speech")

    file_name = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(TEMP_AUDIO_DIR, file_name)

    tts = gTTS(text)
    tts.save(file_path)

    return file_path

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Talk App Backend!"}

# Upload and process image
@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    text = extract_text_from_image(file.file)
    audio_path = text_to_speech(text)
    return FileResponse(audio_path, media_type="audio/mp3", filename="output.mp3")

# Upload and process PDF
@app.post("/process-pdf/")
async def process_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file.read())
    audio_path = text_to_speech(text)
    return FileResponse(audio_path, media_type="audio/mp3", filename="output.mp3")

# Process plain text
@app.post("/process-text/")
async def process_text(text: str):
    audio_path = text_to_speech(text)
    return FileResponse(audio_path, media_type="audio/mp3", filename="output.mp3")
