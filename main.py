import tkinter
from tkinter import filedialog
import requests
import json
import base64
import PyPDF2
import wave


# API Key for Eden AI (replace with your actual API key)
PRODUCTION_API_KEY = ""

# API endpoint for Eden AI
URL = "https://api.edenai.run/v2/audio/text_to_speech"

# Headers for the HTTP request
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {PRODUCTION_API_KEY}",
    "Content-Type": "application/json"
}

# Prevents an empty tkinter window from appearing
tkinter.Tk().withdraw()

# Ask the user to select a PDF file
pdf = filedialog.askopenfile(mode='r', title='Select PDF File', initialdir='./', filetypes=[('PDF Files', '*.pdf')])

# Read the PDF file and extract text from each page
reader = PyPDF2.PdfReader(pdf.name)
pdf_text = ''
for i in range(len(reader.pages)):
    page = reader.pages[i]
    pdf_text += page.extract_text()

# Payload for the Eden AI API request
payload = {
    "response_as_dict": "true",
    "attributes_as_list": "false",
    "show_original_response": "false",
    "providers": "google",
    "fallback_providers": "amazon",
    "language": "en",
    "option": "MALE",
    "text": pdf_text,
    "rate": "0",
    "pitch": "0",
    "volume": "0",
    "sampling_rate": "0",
}

# Make a POST request to the Eden AI API
response = requests.post(URL, params=payload, headers=headers)
response.raise_for_status()

# Parse the JSON response
result = json.loads(response.text)
base64_string = result['google']['audio']

# Decode the Base64-encoded audio data
decoded = base64.b64decode(base64_string)

# Write the decoded audio data to a WAV file
with wave.open("output.mp3", "wb") as wav_file:
    # Set audio parameters (you may need to adjust these based on your specific case)
    wav_file.setnchannels(2)  # Mono
    wav_file.setsampwidth(2)  # 16-bit
    wav_file.setframerate(44100)  # Sample rate

    # Write the binary data to the WAV file
    wav_file.writeframes(decoded)
