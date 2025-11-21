# 11.Write a program that prints the multiplication table of any number entered by
# the user using a for loop.
# Example Output:

# Enter number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# ...
# 6 x 10 = 60

n=int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
    