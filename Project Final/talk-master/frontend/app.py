import streamlit as st
from PIL import Image
import tempfile
import os
import time
from gtts import gTTS
import pytesseract
from pdf2image import convert_from_path

# Import processing functions from your modules
from processing.pdf_processing import extract_text_from_pdf
from processing.image_processing import extract_text_from_image

# Set Tesseract-OCR installation path (Adjust this path based on your OS)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Page Configuration
st.set_page_config(
    page_title="TALK-Master: Text to Speech Converter",
    page_icon="🗣️",
    layout="wide"
)

# Sidebar Theme Toggle
theme = st.sidebar.radio("Select Theme", ["Light Mode", "Dark Mode"])
if theme == "Dark Mode":
    st.markdown(
        """
        <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: #1E1E1E;
            color: white;
        }
        .stTextArea>div>textarea {
            background-color: #1E1E1E;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Header
st.title("🗣️ TALK-Master: Text to Speech Converter")
st.subheader("Convert PDFs, Images, and Text into Speech")

# Dropdown for Input Selection
input_type = st.selectbox(
    'Select Input Type:',
    ['Text', 'PDF', 'Image']
)

# Text Area for User Input
text = ""
file_path = None

if input_type == 'Text':
    text = st.text_area("Enter text here:", height=150)

elif input_type in ['PDF', 'Image']:
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["pdf", "png", "jpg", "jpeg"] if input_type == 'Image' else ['pdf']
    )
    if uploaded_file is not None:
        # Save the file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            file_path = tmp_file.name
            tmp_file.write(uploaded_file.getbuffer())

# Optimized GTTS Processing with Indian Accent
def text_to_speech(text, temp_dir):
    tts = gTTS(text, lang="en", tld="co.in")  # Indian Accent
    file_path = os.path.join(temp_dir, "output.mp3")
    tts.save(file_path)
    return file_path

# Process Input Button
if st.button('Process Input'):
    with tempfile.TemporaryDirectory() as temp_dir:
        if input_type == 'Text' and text:
            audio_file_path = text_to_speech(text, temp_dir)
            st.audio(audio_file_path, format='audio/mp3', start_time=0)
            st.success("🎉 Audio generated successfully!")

        elif input_type in ['PDF', 'Image'] and file_path:
            extracted_text = extract_text_from_pdf(file_path) if input_type == 'PDF' else extract_text_from_image(file_path)
            if extracted_text:
                st.write("### Extracted Text:")
                st.write(extracted_text)

                audio_file_path = text_to_speech(extracted_text, temp_dir)
                st.audio(audio_file_path, format='audio/mp3', start_time=0)
                st.success("✅ Processing complete, audio is ready!")
            else:
                st.error("❌ No text extracted. Please check the input file.")

# Sidebar with App Info
st.sidebar.image("docs/icon.jpg", use_container_width=True)  # Replace with an actual logo
st.sidebar.markdown("Made with ❤️ using Streamlit")

