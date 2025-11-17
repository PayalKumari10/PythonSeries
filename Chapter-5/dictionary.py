#Dictionary Basics

student= {
    "name" : "Payal Kumari",
    "age" : 25,
    "city" : "Ara",
    "rollNumber" : 28,
    "city": "Delhi"
}

print(type(student))
print(student["city"])
print(student)
print(student["name"])
# student["city"]= "Banglore"
print(student)
student["favSubject"]= "Computer"
print(student)
student.pop("favSubject")
print(student)
print(student.keys())
