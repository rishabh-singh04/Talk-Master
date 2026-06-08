# 🗣️ Talk-Master: Text-to-Speech Converter

Talk-Master is a python-based application that extracts text from **Images**, **PDFs**, and **Plain Text** using OCR (Optical Character Recognition) and converts it to speech/audio (.mp3 files) using Google Text-to-Speech (gTTS).

This repository contains two main interfaces:
1. **FastAPI Backend**: A RESTful API that handles OCR processing and audio generation.
2. **Streamlit Frontend**: A responsive, web-based UI with light/dark theme support for direct interactive use.

---

## 🛠️ Prerequisites

Before running the application, make sure you have the following installed on your system:

### 1. Python
Install **Python 3.8 or above**. Ensure that Python is added to your system environment variables (`PATH`).

### 2. Tesseract OCR (Required for OCR)
The application relies on Tesseract OCR to read text from images and PDF files.
* **Windows**:
  1. Download and install the Tesseract installer (e.g., from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)).
  2. Install it to the default directory: `C:\Program Files\Tesseract-OCR` (the code expects this path).
  3. Ensure it is added to your system `PATH`.
* **Ubuntu/Linux**:
  ```bash
  sudo apt update
  sudo apt install tesseract-ocr
  ```
* **macOS**:
  ```bash
  brew install tesseract
  ```

### 3. Poppler (Required for PDF processing)
`pdf2image` requires Poppler to convert PDF pages into images for OCR.
* **Windows**: 
  1. Download Poppler for Windows (e.g., from [conda-forge](https://github.com/oschwartz10612/poppler-windows/releases)).
  2. Extract the folder and add the path to the `bin` directory of Poppler to your system environment variables (`PATH`).
* **Ubuntu/Linux**:
  ```bash
  sudo apt install poppler-utils
  ```
* **macOS**:
  ```bash
  brew install poppler
  ```

---

## 🚀 Installation & Setup

Navigate to the project folder (`Project Final/talk-master`) and follow these setup steps:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   * **Windows (Command Prompt)**:
     ```cmd
     .\venv\Scripts\activate
     ```
   * **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Running the Applications

You can run either the interactive Streamlit web interface or the FastAPI backend server.

### Option A: Run the Streamlit Frontend Web App
To launch the interactive user interface:
```bash
streamlit run frontend/app.py
```
* Once started, the app will open automatically in your default browser at `http://localhost:8501`.
* It provides a simple file-uploader for PDFs/Images and a text input field, along with a theme toggle in the sidebar.

### Option B: Run the FastAPI Backend Server
To launch the REST API server:
```bash
uvicorn backend.main:app --reload
```
* The backend server will run at `http://127.0.0.1:8000`.
* You can access the auto-generated Swagger API documentation to test the endpoints directly by visiting: **`http://127.0.0.1:8000/docs`**

#### Available API Endpoints:
* `GET /` - Root status message.
* `POST /process-image/` - Upload an image file to get the generated MP3 speech file back.
* `POST /process-pdf/` - Upload a PDF file to get the generated MP3 speech file back.
* `POST /process-text/` - Send a text query parameter to get the generated MP3 speech file back.