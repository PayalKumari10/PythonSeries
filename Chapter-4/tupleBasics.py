#tuples Basics

myTuple=(78, 90, 100)
studentTuple=("Payal", "Ram", "Sita")

# studentTuple[1] = "ruchi"  # This will raise an error because tuples are immutable

print(studentTuple[2])

#empty tuple
emptyTuple= ()
singleTuple= (1,) 
singleTuple= (1) #integer
print(type(emptyTuple))
print(type(singleTuple))
print(studentTuple.index("Sita"))
print(studentTuple.count("Ram"))