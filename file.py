import os
import shutil

# Define file type mappings
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Music': ['.mp3', '.wav', '.aac', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
    'Others': []
}

def get_file_category(file_extension):
    """Return the category of a file based on its extension."""
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(directory):
    """Organize files in the given directory into categorized folders."""
    if not os.path.isdir(directory):
        print("Invalid directory!")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1]
            category = get_file_category(file_ext)

            category_folder = os.path.join(directory, category)
            os.makedirs(category_folder, exist_ok=True)

            # Move the file to the appropriate folder
            new_path = os.path.join(category_folder, filename)
            shutil.move(file_path, new_path)
            print(f"Moved: {filename} → {category}/")

    print("\n✅ All files organized successfully!")

# Example usage
if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to organize: ")
    organize_files(folder_path)
