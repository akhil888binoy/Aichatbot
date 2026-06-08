
import requests
from dotenv import load_dotenv
import os

load_dotenv()
ollama_api = os.getenv('OLLAMA_API').strip()

def test_connection():
    try:
        response = requests.get(f"{ollama_api}/api/tags")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")
        return False

def send_ollama(prompt, model="qwen"):
    response = requests.post(
        f"{ollama_api}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

