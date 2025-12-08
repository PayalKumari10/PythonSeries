class Student:
    schoolName= "ABC School"

    def __init__(self, name, course):
        # print("whenver a new object is created I am called automaticaly")
        # print(self)
        self.name= name
        self.cousre= course

student1= Student("Payal", "MCA") #init method will be called
print("Student1 Name-", student1.name)
print("Student1 Course-", student1.cousre)

student2= Student("Radha", "MCA")
print("Student2 Name-", student2.name)
print("Student2 Course-", student2.cousre)
