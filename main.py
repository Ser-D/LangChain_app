from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import json
from langchain import HuggingFaceHub
import os
import logging
import warnings
from dotenv import load_dotenv


# Ignore warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

class TextRequest(BaseModel):
    text: str = (
        "Artificial intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. "
        "These processes include learning (the acquisition of information and rules for using it), reasoning (using rules to reach approximate or definite conclusions), "
        "and self-correction. Specific applications of AI include expert systems, speech recognition, and machine vision."
    )

class TextResponse(BaseModel):
    summary: str

# Set Hugging Face API token
api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Initialize the Hugging Face model via LangChain
llm = HuggingFaceHub(
    repo_id='facebook/bart-large-cnn',
    model_kwargs={"temperature": 0.7, "max_length": 180, 'top_k': 10, 'top_p': 0.95, 'repetition_penalty': 1.03},
    huggingfacehub_api_token=api_token
)

@app.post("/summarize", response_model=TextResponse)
async def summarize(request: TextRequest):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required.")

    # Summarize the text
    try:
        logging.info("Invoking summarization model...")
        summary = llm.invoke(f"Summarize the following text:\n\n{text}")
        logging.info("Summarization successful.")
    except Exception as e:
        logging.error(f"Error during summarization: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    # Save the data to a JSON file
    with open("summary.json", "w", encoding="utf-8") as file:
        json.dump({"text": text, "summary": summary}, file, ensure_ascii=False, indent=4)

    return TextResponse(summary=summary)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="127.0.0.1", port=8001)
