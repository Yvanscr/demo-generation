import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('HUGGING_FACE_TOKEN')

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

TEXT_API_URL = "https://api-inference.huggingface.co/models/gpt2"
IMAGE_API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"