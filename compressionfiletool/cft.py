import zipfile
import os

def compress_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_path)

def main():
    print("File Compression Tool")
    print("1. Compress Folder")
    print("2. Extract ZIP")
    choice = input("Enter your choice: ")

    if choice == '1':
        folder_path = input("Enter the folder path to compress: ")
        zip_path = input("Enter the ZIP file path to save: ")
        compress_folder(folder_path, zip_path)
        print("Folder compressed successfully!")
    elif choice == '2':
        zip_path = input("Enter the ZIP file path to extract: ")
        extract_path = input("Enter the extraction path: ")
        extract_zip(zip_path, extract_path)
        print("ZIP file extracted successfully!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
