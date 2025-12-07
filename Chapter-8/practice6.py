# 1 . Use with to read the entire content of info.txt
import os
with open("info.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Output of readlines method:", lines)


# 2 . Use with to write "Hello World" in hello.txt.

with open("hello.txt", "w", encoding="utf-8") as f:
    lines = f.write("Hello World!")
    print("Output of write method:", lines)


os.rename("Saumya.txt", "Payal.txt")
