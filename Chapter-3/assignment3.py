#Write a program that takes a sentence and prints:
#1. Total characters(len())
#2. Uppercase version
#3. Lowercase version


sentence = input("enter a sentence: ")
print("Toatl charcters: ", len(sentence))
print("Uppercase version: ", sentence.upper())
print("Lowercase version: ", sentence.lower())

#Q2. Write a Python program that takes any word or sentence as input and prints:
#1. The first character
#2. The last character
#3. The total number of characters

word = input("Enter a word or sentence: ")
print("First character: ", word[0])
print("Last character: ", word[-1])
print("Total number of characters: ", len(word))
