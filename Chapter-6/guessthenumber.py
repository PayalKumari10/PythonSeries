# Mini Project – Guess the Number Game
# Concepts Used: while loop and user input.
# Sample Run:
# Guess a number between 1 and 10: 4
# Wrong guess! Try again.
# Guess again: 7
# Congratulations, Payal! You guessed it right 🎉

import random
number_to_guss = random.randint(1, 10)
user_guess = None
while user_guess != number_to_guss:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == number_to_guss:
        print("Congratulations, Payal! You guessed it right 🎉")
    else:
        print("Wrong guess! Try again.")
