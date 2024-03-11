from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    """
    Convert text to speech and save it as an audio file.
    
    Parameters:
        text (str): The text to convert to speech.
        lang (str): Language code (default is 'en' for English).
    
    Returns:
        str: Filename of the generated audio file.
    """
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang)
    
    # Save the audio file
    filename = "output.mp3"
    tts.save(filename)
    
    return filename

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    filename = text_to_speech(text)
    
    # Play the generated audio file
    os.system("start " + filename)
