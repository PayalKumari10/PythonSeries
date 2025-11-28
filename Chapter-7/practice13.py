# Create a function full_name(fname, lname) that returns the full name joined with a space.

def full_name(fname, lname):
    return f"{fname} {lname}"

print(full_name("Payal", "Kumari")) 



# Write a program with a local variable score inside a function and a global one outside.

def show_score():
    score = 90  
    return f"Local Score: {score}"



# Create a program using global keyword to modify a variable from inside a function.

def modify_global():
    global level
    level = "Intermediate"
    return f"Modified Level: {level}"
level = "Beginner"
print(show_score())
print(f"Global Level before modification: {level}")
print(modify_global())
print(f"Global Level after modification: {level}")


# Explain the difference between local and global scope in your own words.

def explain_scope():
    return ("Local scope refers to variables defined within a function, "
            "which can only be accessed inside that function. "
            "Global scope refers to variables defined outside any function, "
            "which can be accessed from anywhere in the code.")
print(explain_scope())
