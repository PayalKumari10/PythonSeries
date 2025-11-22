# 1. Print numbers from 1 to 100 using a for loop.
for i in range(1, 101):
    print(i)

print("Completed printing numbers from 1 to 100")

# 2. Print numbers from 100 to 1 using a while loop.
count = 100
while count >= 1:
    print(count)
    count -= 1
print("Completed printing numbers from 100 to 1")


# 3. Print all numbers between 1 and 50 except multiples of 5.
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)
    print("Completed printing numbers between 1 and 50 except multiples of 5")

# 4. Create a program that asks the user for 5 favorite foods and prints them one by one.

foods = ["Cholcolate", "Ice Cream", "Pizza", "Burger", "Pasta"]

for food in foods:
    print(food)
print("Completed printing favorite foods")

# 5. Print the sum of first 10 natural numbers using a while loop.

sum = 0
num = 1
while num <= 10:
    sum += num
    num += 1
print("The sum of first 10 natural numbers is:", sum)
print("Completed calculating the sum of first 10 natural numbers")