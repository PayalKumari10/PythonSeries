# Q1 Ask the user for their 3 favorite movies and store them in a list.

favorite_movies = ["English Vinglish", "3 Idiots", "PK"]

print("My favorite movies are:")
for movie in favorite_movies:
    print(movie)

# Ask user for 3 movies
asked_movies = input("Enter your 3 favorite movies separated by commas: ")

# Convert string to list
user_movies = [movie.strip() for movie in asked_movies.split(",")]

print("\nYour favorite movies are:")
for movie in user_movies:
    print(movie)


# Q2 Create a tuple of marks(87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min().

marksTuple = (87, 64, 33, 95, 76)
highest_mark = max(marksTuple)
lowest_mark = min(marksTuple)
print(f"\nHighest mark: {highest_mark}")
print(f"Lowest mark: {lowest_mark}")


# Q3 Write a  program to check grade based on marks (A/B/C/D) using if-elif-else.
marks=int(input("\nEnter your marks (0-100): "))
if marks >= 90:
     grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else: 
    grade = 'F'
print(f"Your grade is: {grade}")
        
