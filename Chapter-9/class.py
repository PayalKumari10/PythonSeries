#class creation
class Vehicle:
    color="black"   #attributes
    petrolOrDisel="petrol" #attributes
    mileage="20"    #attributes

    def start():  #methods
        print("When you press clutch and acclerator then vehicle is start")

#object creation
car=Vehicle()
print(car.color)

bike= Vehicle()
print(bike.color)

aeroplane= Vehicle()
print(aeroplane.mileage)
print(aeroplane.color)

#we created one class an 3 objects of that class

