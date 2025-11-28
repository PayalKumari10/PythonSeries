# Create a function full_name(fname, lname) that returns the full name joined with a space.

def full_name(fname, lname):
    return f"{fname} {lname}"

print(full_name("Payal", "Kumari")) 



# Write a program with a local variable score inside a function and a global one outside.

def show_score():
    score = 90  
    return f"Local Score: {score}"