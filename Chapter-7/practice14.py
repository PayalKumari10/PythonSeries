# Write a recursive function that prints numbers from 1 to N.

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)

print(print_numbers(5))
        

# Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Write a recursive function to print the Fibonacci series up to N terms.
def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=' ')
        fibonacci(n - 1, b, a + b)
print(fibonacci(7))        