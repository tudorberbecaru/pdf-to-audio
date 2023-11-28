# PDF-to-Audio Converter

Convert PDF documents into audio files using Eden AI's Text-to-Speech (TTS) service.

## Overview

This script leverages the Eden AI API to convert text extracted from PDF documents into spoken audio. The Text-to-Speech service supports multiple providers, including Google, Amazon, Microsoft and IBM, allowing for flexibility in choosing voices and styles.

## Requirements

- Python 3.x
- PyPDF2 3.0.1
- requests 2.31.0

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tudorberbecaru/pdf-to-audio.git

2. Navigate to the project directory:

   ```bash
   cd pdf-to-audio
   
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Usage

1. **Create an Account on Eden AI's Website:**
   - Go to [Eden AI's website](https://www.edenai.co/).
   - Click on `Start building`
   - Create an account and obtain your free production (not sandbox) API key.

2. **Insert API Key in `main.py`:**
   - Replace the `PRODUCTION_API_KEY` variable in `main.py` with your actual API key.

3. **Run the Script:**
   - Execute the script: `python main.py`
   - The script will prompt you to select a PDF file, and it will generate an audio file (output.mp3) based on the extracted text.

## Configuration

- Customize TTS options such as language, voice, rate, pitch, volume, and more by modifying the `payload` dictionary in `main.py`. For detailed information about each parameter, refer to [this link](https://docs.edenai.co/reference/audio_text_to_speech_create).
- Adjust audio parameters (channels, sample width, sample rate) in the `wav_file` settings to meet your requirements.

## Acknowledgments

- Eden AI for providing the Text-to-Speech service.

## Contributing

Contributions are welcome! Feel free to modify any part of the code according to your preferences.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
