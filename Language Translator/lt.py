from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def translate_file(file_path, target_language='en'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            translated_content = translate_text(content, target_language)
            
        output_file_path = f"{file_path}_translated_{target_language}.txt"
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(translated_content)
        
        print(f"Translation saved to: {output_file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Language Translator")

    while True:
        print("\nOptions:")
        print("1. Translate Text")
        print("2. Translate File")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, 3): ")

        if choice == '1':
            text = input("Enter the text to translate: ")
            target_language = input("Enter the target language code (e.g., 'fr' for French): ")
            translated_text = translate_text(text, target_language)
            print(f"\nTranslated Text: {translated_text}")

        elif choice == '2':
            file_path = input("Enter the path to the file for translation: ")
            target_language = input("Enter the target language code (e.g., 'fr' for French): ")
            translate_file(file_path, target_language)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
