import os
import shutil

# Apne TestFolder ka path yahan daalo
folder_path = r"c:\Users\NIRAV\Desktop\krisha\test folder"

# Folder names
image_folder = os.path.join(folder_path, "Images")
pdf_folder = os.path.join(folder_path, "PDFs")
text_folder = os.path.join(folder_path, "TextFiles")
video_folder = os.path.join(folder_path, "Videos")

# Folders create karo
os.makedirs(image_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)

# Files read karo
for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Images
    if file.endswith((".jpg", ".jpeg", ".png")):
        shutil.move(file_path, os.path.join(image_folder, file))

    # PDFs
    elif file.endswith(".pdf"):
        shutil.move(file_path, os.path.join(pdf_folder, file))

    # Text files
    elif file.endswith(".txt"):
        shutil.move(file_path, os.path.join(text_folder, file))

    # Videos
    elif file.endswith(".mp4"):
        shutil.move(file_path, os.path.join(video_folder, file))

print("Files Organized Successfully!")