def countVowConso(userInput):

    vowels = "aeiouAEIOU"
    countVowels = 0
    countConsonants = 0

    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowels += 1
            else:
                countConsonants += 1

    return countVowels, countConsonants  


# Function Call                
vowels, consonants = countVowConso("Hello World")
print(vowels, consonants)
