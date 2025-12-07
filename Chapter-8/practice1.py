#Write a program to read a text from a given file certificate.txt and find wheather it contains the word live.


file = open("certificate.txt", "r", encoding="utf-8")
dataOfFile = file.read()

dataOfFile= dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes, the word live is present in the file.")
else:
    print("No, the word live is not present in the file.")


# What happens if you open a non-existing file in "r" mode?
# It raises a FileNotFoundError.
