from src.generate import generate_text, generate_image, save_text_to_file

def main():
    # Demander à l'utilisateur d'entrer un prompt
    user_prompt = input("Enter a prompt to generate text and an image : ")

    # Générer du texte
    print("\nGenerating text...")
    try:
        generated_text = generate_text(user_prompt)
        print("Texte généré :")
        print(generated_text)
        
        text_file_path = save_text_to_file(generated_text, user_prompt)
        print(f"Saved text in : {text_file_path}")
    except Exception as e:
        print(f"Error : {e}")

    # Générer une image
    print("\nGenerating image...")
    try:
        image_path = generate_image(user_prompt)
        print(f"Saved the image at : {image_path}")
    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    main()