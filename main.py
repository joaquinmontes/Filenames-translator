import os
from googletrans import Translator
from time import sleep

def translate_filenames():
    translator = Translator()
    
    # Get the directory of the current script (main.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the path to the 'files' folder inside the 'Filenames-translator' directory
    path = os.path.join(script_dir, 'files_to_rename')
    
    # Check if the path exists
    if not os.path.exists(path):
        print(f"The directory '{path}' does not exist, please create a 'files to rename' folder inside Filenames-translator.")
        return

    files = os.listdir(path)
    print(f"Processing files in: {path}")

    for file in files:
        filename, file_ext = os.path.splitext(file)
        
        if filename:
            try:
                # Translate the filename
                translation = translator.translate(filename, src='en', dest='es')

                # Check if translation was successful
                if translation and hasattr(translation, 'text'):
                    new_filename = translation.text
                    # Construct full path for renaming
                    old_file_path = os.path.join(path, file)
                    new_file_path = os.path.join(path, new_filename + file_ext)

                    # Rename the file
                    os.rename(old_file_path, new_file_path)
                    print(f"{file} -> {new_filename + file_ext}")
                else:
                    print(f"Translation failed for '{filename}'. Response: {translation}")
                
                sleep(1)  # Pause to avoid rate limiting
            except Exception as e:
                print(f"Error translating '{filename}': {e}")

if __name__ == "__main__":
    translate_filenames()
