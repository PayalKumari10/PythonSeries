# Create a class laptop with attributes: brand, RAM, price. Create 2 objects with different values.

class Laptop:
    brand= "default"
    RAM= "default 8GB"
    price= "1 Lakh"

laptop1= Laptop()
laptop1.brand= "Macbook"   #attribute
laptop1.RAM= "32GB"        #attribute
print("Laptop1 Brand -- ", laptop1.brand)

laptop2= Laptop()
laptop2.brand= "Dell"     #attribute
laptop2.RAM= "16GB"       #attribute
laptop2.price= "75,000"    
print("Laptop2 Brand -- ", laptop2.brand)

