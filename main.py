import os
import time
from googletrans import Translator, LANGUAGES
from time import sleep

def translate_filenames():
    translator = Translator()
    path = os.getcwd()
    files = os.listdir(path)

    for file in files:
        filename, file_ext = os.path.splitext(file)
        
        # Skip specific filenames
        if filename and filename not in ['main', 'start']:
            sleep(5)
            try:
                # Translate the filename
                translation = translator.translate(filename, src='en', dest='es')

                # Check if translation was successful
                if translation and hasattr(translation, 'text'):
                    new_filename = translation.text
                    # Rename the file
                    os.rename(file, new_filename + file_ext)
                    print(f"{file} -> {new_filename + file_ext}")
                else:
                    print(f"Translation failed for '{filename}'. Response: {translation}")
                
                time.sleep(1)  # Pause to avoid rate limiting
            except Exception as e:
                print(f"Error translating '{filename}': {e}")

if __name__ == "__main__":
    translate_filenames()
