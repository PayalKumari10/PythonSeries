# Count how many words are present in the file notes.txt.


with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    words = content.split()   # split() breaks text into words
    print("Total words:", len(words))


# Append the current date and time to a file logs.txt whenver the program runs.

from datetime import datetime

# Get current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Append to logs.txt
with open("logs.txt", "a", encoding="utf-8") as f:
    f.write(current_time + "\n")

print("Log updated.", current_time)


