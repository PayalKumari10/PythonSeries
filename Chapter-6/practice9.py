#Write a program to print numbers from 1 to 50, but print "Payal Kumari"
#instead of numbers that are multiples of 5.
#Example Output: 1 2 3 4 Payal Kuamri 6 7 8 9 Payal Kumari

n = 1

while n <= 50:
    if n % 5 == 0:
        print("Payal Kumari")
    else:
        print(n)
    n = n + 1
print("We are out of the while loop and value of n is:", n) 
