# Print how many lines are present in notes.txt

with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    number_of_lines = len(lines)
    print("Output of readlines method:", lines)
    print("Number of lines in notes.txt:", number_of_lines)