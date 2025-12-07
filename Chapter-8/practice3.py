# Read only the line of bio.txt

with open("bio.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    print("Line 1:", line1)