#Q1 Create a dictionary storing meanings of 3 English words
words= {
    "Code": "To write instructions for a computer",
    "Eat": "To take in food",
    "Repeat": "To do something again"
}

print(words)


#Q2 Create a set of numbers and show union and intersection with another set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))


#Q3 Try to add both integer 9 and float 9.0 to a set and observe what happens. 
# (Hint : You can convert one into a string to make both unique.)

my_set = {9, 9.0}
print(my_set)   # Only one value will appear

# To make both unique, convert one to a string
my_set_unique = {9, "9.0"}
print(my_set_unique)