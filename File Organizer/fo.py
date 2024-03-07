import os
import shutil

def organize_files(source_dir):
    # Dictionary to hold file extensions and corresponding directory names
    extensions = {
        'Documents': ['.txt', '.doc', '.docx', '.pdf', '.xlsx', '.pptx', '.csv'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Music': ['.mp3', '.wav', '.ogg', '.flac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar.gz'],
        'Executables': ['.exe', '.msi']
    }

    # Create directories if they do not exist
    for folder in extensions.keys():
        if not os.path.exists(os.path.join(source_dir, folder)):
            os.mkdir(os.path.join(source_dir, folder))

    # Move files to respective directories
    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file)):
            for folder, ext_list in extensions.items():
                if any(file.lower().endswith(ext) for ext in ext_list):
                    shutil.move(os.path.join(source_dir, file), os.path.join(source_dir, folder, file))
                    print(f"Moved {file} to {folder}")
                    break

if __name__ == "__main__":
    source_directory = input("Enter the path of the directory to organize: ")
    organize_files(source_directory)
