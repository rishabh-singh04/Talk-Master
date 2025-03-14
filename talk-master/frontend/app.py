# import streamlit as st
# from PIL import Image
# import requests
# from bs4 import BeautifulSoup
# from gtts import gTTS
# import pytesseract
# from pdf2image import convert_from_path
# import cv2
# import numpy as np
# import os
# import tempfile
# import time
# import shutil

# # Import processing functions from your custom modules
# from processing.pdf_processing import extract_text_from_pdf
# from processing.image_processing import extract_text_from_image
# from processing.text_to_speech import text_to_speech

# # Set Tesseract-OCR installation path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Setup page configuration
# st.set_page_config(page_title="TALK-Master: Text to Speech Converter", page_icon="🗣️")

# # Title and welcome animation
# st.title("TALK-Master: Text to Speech Converter")
# placeholder = st.empty()
# for seconds in range(3):
#     placeholder.markdown(f"<p style='color: blue; font-size: {26 + seconds * 8}px;'>Welcome to TALK-Master</p>", unsafe_allow_html=True)
#     time.sleep(0.5)
# placeholder.empty()

# # Tesseract-OCR configuration (adjust based on your installation)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Text-to-Speech Function
# def text_to_speech(text, temp_dir):
#     tts = gTTS(text)
#     file_path = os.path.join(temp_dir, "output.mp3")
#     tts.save(file_path)
#     return file_path

# # Selection of input type
# input_type = st.selectbox('Select input type:', ['PDF', 'Image', 'Text'])
# text = ""
# file_path = None

# if input_type == 'Text':
#     text = st.text_area("Enter text here:", height=150)

# elif input_type in ['PDF', 'Image']:
#     uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"] if input_type == 'Image' else ['pdf'])
#     if uploaded_file is not None:
#         with tempfile.NamedTemporaryFile(delete=True, suffix=uploaded_file.name[uploaded_file.name.rfind('.'):]) as tmp_file:
#             file_path = tmp_file.name
#             tmp_file.write(uploaded_file.getbuffer())

# # Processing button
# if st.button('Process Input'):
#     with tempfile.TemporaryDirectory() as temp_dir:
#         try:
#             if input_type == 'Text' and text:
#                 audio_file_path = text_to_speech(text, temp_dir)
#                 st.audio(audio_file_path, format='audio/mp3', start_time=0)
#                 st.success("Text processed and audio ready to play below!")

#             elif input_type in ['PDF', 'Image'] and file_path:
#                 extracted_text = extract_text_from_pdf(file_path) if input_type == 'PDF' else extract_text_from_image(file_path)
#                 if extracted_text:
#                     st.write("Extracted Text:")
#                     st.write(extracted_text)
#                     audio_file_path = text_to_speech(extracted_text, temp_dir)
#                     st.audio(audio_file_path, format='audio/mp3', start_time=0)
#                     st.success("Processing complete and audio ready to play below!")
#                 else:
#                     st.error("No text extracted. Please check the input file and try again.")

#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")


# UPLOAD_FOLDER = 'uploaded_files'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # File uploader widget
# uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     # Construct a full path to save the file
#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    
#     # Write the uploaded file to the new path
#     with open(file_path, "wb") as f:
#         shutil.copyfileobj(uploaded_file, f)

#     st.success(f"Uploaded file saved to {file_path}.")

#     try:
#         # Process the file
#         # For example, here you might call a function like:
#         # text = extract_text_from_image(file_path)
#         # And then use the `text` for further processing or display
#         st.write("Processing file... (implement processing logic here)")
        
#         # Optionally, display the file (if image)
#         if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
#             st.image(file_path, caption='Uploaded Image')

#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")

#     finally:
#         # Clean up: remove file after processing if not needed
#         # os.remove(file_path)
#         # st.info("Temporary file deleted.")
#         pass

# else:
#     st.warning("Please upload a file.")

# # Sidebar and additional UI elements
# st.sidebar.image("https://th.bing.com/th/id/R.a0f02b6739a4bc7391fdea282f5cb5fb?rik=XJoHzQc4zru2Vg&riu=http%3a%2f%2fis4.mzstatic.com%2fimage%2fthumb%2fPurple62%2fv4%2fd6%2ff9%2fc0%2fd6f9c0f4-7956-c614-167b-de9e5630740c%2fsource%2f1200x630bb.jpg&ehk=eUPHiW3wArh3LRKGlwiy15YdZhKi226Hsv2PJZ64CXE%3d&risl=&pid=ImgRaw&r=0", use_container_width=True)  # Replace with actual path to logo
# st.sidebar.text("Made with ❤️ and Streamlit")


import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np
import os
import tempfile
import time
import shutil

# Import processing functions from your custom modules
from processing.pdf_processing import extract_text_from_pdf
from processing.image_processing import extract_text_from_image
from processing.text_to_speech import text_to_speech

# Set Tesseract-OCR installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Setup page configuration
st.set_page_config(page_title="TALK-Master: Text to Speech Converter", page_icon="🗣️")

# Title and welcome animation
st.title("TALK-Master: Text to Speech Converter")
placeholder = st.empty()
for seconds in range(3):
    placeholder.markdown(f"<p style='color: blue; font-size: {26 + seconds * 8}px;'>Welcome to TALK-Master</p>", unsafe_allow_html=True)
    time.sleep(0.5)
placeholder.empty()

# Text-to-Speech Function
def text_to_speech(text, temp_dir):
    tts = gTTS(text)
    file_path = os.path.join(temp_dir, "output.mp3")
    tts.save(file_path)
    return file_path

# Selection of input type
input_type = st.selectbox('Select input type:', ['PDF', 'Image', 'Text'])
text = ""
file_path = None

if input_type == 'Text':
    text = st.text_area("Enter text here:", height=150)
elif input_type in ['PDF', 'Image']:
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"] if input_type == 'Image' else ['pdf'], key='input_file_uploader')
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=True, suffix=uploaded_file.name[uploaded_file.name.rfind('.'):]) as tmp_file:
            file_path = tmp_file.name
            tmp_file.write(uploaded_file.getbuffer())

# Processing button
if st.button('Process Input'):
    with tempfile.TemporaryDirectory() as temp_dir:
        if input_type == 'Text' and text:
            audio_file_path = text_to_speech(text, temp_dir)
            st.audio(audio_file_path, format='audio/mp3', start_time=0)
            st.success("Text processed and audio ready to play below!")

        elif input_type in ['PDF', 'Image'] and file_path:
            extracted_text = extract_text_from_pdf(file_path) if input_type == 'PDF' else extract_text_from_image(file_path)
            if extracted_text:
                st.write("Extracted Text:")
                st.write(extracted_text)
                audio_file_path = text_to_speech(extracted_text, temp_dir)
                st.audio(audio_file_path, format='audio/mp3', start_time=0)
                st.success("Processing complete and audio ready to play below!")
            else:
                st.error("No text extracted. Please check the input file and try again.")

# Sidebar and additional UI elements
st.sidebar.image("docs/icon.jpg", use_container_width=True)  # Replace with actual path to logo
st.sidebar.text("Made with Streamlit")
