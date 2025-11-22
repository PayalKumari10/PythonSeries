# Mini Project – Multiplication Table
# Goal: Print the multiplication table of a number using a loop.
# Sample Run:
# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50




num = int(input("Enter a number: "))

for i in range(1, 10 + 1):
    print(num, "x", i, "=", num * i)
