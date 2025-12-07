# 1. Write your name and class into a file named intro.txt

with open("intro.txt", "w", encoding="utf-8") as f:
    f.write("Name: Payal Kumari\n")
    f.write("Class: 10th Grade\n")
    print("Intro file created with name and class.")


with open("intro.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Content of intro.txt:")
    print(content)    


# 2. Create a file goals.txt and write 3 goals for the month

with open("goals.txt", "w", encoding="utf-8") as f:
    f.write("1. Complete Python course\n")
    f.write("2. Read 2 books\n")
    f.write("3. Exercise daily\n")
    print("Goals file created with 3 goals for the month.")


with open("goals.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Content of goals.txt:")
    print(content)


# 3. Append "Completed" to an existing file status.txt

with open("status.txt", "a", encoding="utf-8") as f:
    f.write("Completed\n")
    print("Appended 'Completed' to status.txt.")

with open("status.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Content of status.txt:")
    print(content)    