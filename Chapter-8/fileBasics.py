file = open("mast.txt", "r", encoding="utf-8")
data = file.read()

print("Data of the file is:", data)
file.close()
