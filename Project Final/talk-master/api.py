from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
import pytesseract
from PIL import Image
import numpy as np
from gtts import gTTS
import requests
from bs4 import BeautifulSoup
from pdf2image import convert_from_bytes
import cv2

app = FastAPI()

@app.post("/text-to-speech/")
async def text_to_speech(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    return FileResponse("temp.mp3")

@app.post("/scrape/")
async def scrape(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="No URL provided")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return {"content": soup.prettify()}

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return Image.fromarray(gray)

@app.post("/pdf-to-image/")
async def pdf_to_image(file: UploadFile = File(...)):
    contents = await file.read()
    images = convert_from_bytes(contents)
    for i, image in enumerate(images):
        image.save(f'page_{i}.png', 'PNG')
    return {"message": "Images saved successfully"}