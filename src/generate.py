import re
import requests
from PIL import Image
from io import BytesIO
from src.config import HEADERS, TEXT_API_URL, IMAGE_API_URL

# Fonction pour générer du texte
def generate_text(prompt):
    payload = {"inputs": prompt}
    response = requests.post(TEXT_API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        generated_text = response.json()[0]['generated_text']
        return generated_text
    else:
        raise Exception(f"Error generating text: {response.status_code} - {response.text}")

# Fonction pour générer une image
def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(IMAGE_API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image_name = re.sub(r'\W+', '_', prompt) 
        image_path = f"{image_name}.png"
        image.save(image_path)
        return image_path
    else:
        raise Exception(f"Error generating image: {response.status_code} - {response.text}")
    

def save_text_to_file(text, prompt):
    file_name = re.sub(r'\W+', '_', prompt)
    text_file_path = f"{file_name}.txt"
    
    with open(text_file_path, 'w') as file:
        file.write(text)
    
    return text_file_path
