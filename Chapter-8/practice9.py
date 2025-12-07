try:
    with open("notes.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("File content:", content)

except FileNotFoundError:
    print("The file doesn't exist. Please check the name.")

except Exception as e:
    print("Something went wrong:", e)
