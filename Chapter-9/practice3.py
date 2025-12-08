# Create class Student that takes 3 marks and has a method average()

class Student:

    def __init__(self, name, listOfMarks):
       self.name= name
       self.listOfMarks= listOfMarks

    def average(self):
        sum= 0
        for eachValue in self.listOfMarks:
            sum= sum + eachValue
        average= sum/3    
        print("Average is:" , average)
        
student1= Student("Payal",[99, 98, 97])        
student1.average()


#Create satic method to vaildate if a number is even

class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Test
print(MathUtils.is_even(10))  # True
print(MathUtils.is_even(7))   # False
