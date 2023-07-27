import os
import shutil
import filecmp
import sys

def sync_folders(origin_folder, destination_folder):
    # Get the list of files in the origin folder
    origin_files = set(os.listdir(origin_folder))

    # Get the list of files in the destination folder
    destination_files = set(os.listdir(destination_folder))

    # Synchronize only PDF files from origin to destination
    for file in origin_files:
        if file.lower().endswith(".pdf"):
            origin_file_path = os.path.join(origin_folder, file)
            destination_file_path = os.path.join(destination_folder, file)

            if not os.path.exists(destination_file_path):
                # If the file doesn't exist in destination, copy it from origin
                shutil.copy2(origin_file_path, destination_file_path)
                print(f"Copied: {file}")
            else:
                # If the file exists, compare files to check if update is required
                if not filecmp.cmp(origin_file_path, destination_file_path):
                    # If the files are different, replace the file in destination
                    os.remove(destination_file_path)
                    shutil.copy2(origin_file_path, destination_file_path)
                    print(f"Replaced: {file}")

    # Remove PDF files from destination if they don't exist in origin
    for file in destination_files - origin_files:
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(destination_folder, file)
            os.remove(file_path)
            print(f"Deleted: {file}")


if __name__ == "__main__":
    # origin_folder=""
    # destination_folder=""
    if sys.platform.startswith('darwin'):  # macOS
        origin_folder = "/Users/william.alvarez/Development/Personal/origin"
        destination_folder = "/Users/william.alvarez/Development/Personal/dest"
    elif sys.platform.startswith('win'):  # Windows
            origin_folder = "/Users/william.alvarez/Development/Personal/origin"
            destination_folder = "/Users/william.alvarez/Development/Personal/dest"
    else:
        my_variable = "Unknown platform"
   
    sync_folders(origin_folder, destination_folder)
