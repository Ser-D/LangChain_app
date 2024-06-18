# FastAPI Text Summarizer

## Overview

This FastAPI application accepts a text input and returns a summarized version of the text using the LangChain library with a Hugging Face model.

## Setup

### Prerequisites

- Python 3.11 or higher
- A Hugging Face account and API token

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   
2. **Create a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt

4. **Rename .env.example to .env:**
   ```sh
   mv .env.example .env

4. **Open .env and replace your_hugging_face_api_token with your real API token from Hugging Face**
   ```sh
   HUGGINGFACEHUB_API_TOKEN=your_hugging_face_api_token
   
### Running the Application

1. **Clone the repository:**
   ```sh
   python main.py

2. **Access the documentation:**

- Open your browser and navigate to http://127.0.0.1:8000/docs to test the /summarize endpoint.


## Notes

- Ensure that you replace 'your_hugging_face_api_token' with your actual Hugging Face API token.
- The application saves the summarized text to a summary.json file in the current directory.