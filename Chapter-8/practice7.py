# 1. Copy notes1.txt to notes_backup.txt
import os
import shutil

with open("notes1.txt", "w", encoding="utf-8") as f:
    lines = f.write("Hello World!")
    print("Output of write method:", lines)

# Copy file
shutil.copy("notes1.txt", "notes_backup.txt")
print("File copied successfully!")



# 2. Rename temp.txt to final.txt

with open("temp.txt", "w", encoding="utf-8") as f:
    lines = f.write("Hello World!")
    print("Output of write method:", lines)


# Rename file

# os.rename("temp.txt", "final.txt") 




# 3. Ask user for a filename and copy it to a backup folder.
file_name = input("Enter the filename to back up: ")

# Check if the file exists

if not os.path.exists(file_name):
    print("File not found. Please check the name and try again.")
else:
    #Create backup folder if it doesn't exist
    if not  os.path.exists("backup"):
        os.mkdir("backup")


    #Copy file into backup folder

    backup_path = os.path.join("backup", file_name)
    shutil.copy(file_name, backup_path)      