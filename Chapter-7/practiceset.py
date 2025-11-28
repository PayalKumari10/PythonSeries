# Write a function to calculate the factorial of a number.
def factorial(n):
      if n == 0 or n == 1:
          return 1
      else:
          return n * factorial(n - 1)
      
print(factorial(10))      

# Write a recursive function to print numbers from 1 to N.
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)
print(print_numbers(10))        


# Write a function that checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(29))


# Write a recursive function to find the sum of first N natural numbers.
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)
print(sum_natural(10))    

# Write a function greet_user(name) that prints a personalized message for Payal Kumari.
def greet_user(name):
    return f"Hello, {name}! Welcome aboard."
print(greet_user("Payal Kumari"))


# Write a recursive program to print the reverse of a string.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("Payal"))

# Write a function to return the largest of 3 numbers.
def largest_of_three(a, b, c):
    return max(a, b, c)
print(largest_of_three(10, 25, 15))

# Write a recursive function to print even numbers from 2 to N.
def print_even(n):
    if n >= 2:
        print_even(n - 2)
        if n % 2 == 0:
            print(n)
print(print_even(10))

# Write a function that returns both the sum and average of 5 inputs.
def sum_and_average(a, b, c, d, e):
    total = a + b + c + d + e
    average = total / 5
    return total, average
print(sum_and_average(10, 20, 30, 40, 50))

# Write a program to count vowels in a string using a function.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))