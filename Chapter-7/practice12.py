#Define a function convert_to_upper(word) that returns the uppercase version of the string.

def convert_to_upper(word):
    return word.upper()

print(convert_to_upper("hello")) 

#Define a function message(text="Keep Learning!") and call it with and without an argument.

def message(text="Keep Learning!"):
    return text
print(message())
print(message("Stay Positive!"))


# Create a function login(username, password="1234") that prints the credentials.

def login(username, password="1234"):
    return f"Username: {username}, Password: {password}"
print(login("user1"))
print(login("user2", "abcd"))
