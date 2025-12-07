# With keyword     

# file = open("mast.txt", "r", encoding="utf-8")
# data = file.read()
# print("Data of the file is:", data)
# file.close()



# 1. (Read entire file)

# with open("mast.txt", "r", encoding="utf-8") as file:          
#     data = file.read()
#     print("Data of the file using with keyword is:", data)



# 2. (Read line by line)

# with open("newTextFile.txt", "r", encoding="utf-8") as f:
#    line = f.readline()
#    line2 = f.readline()
#    line3 = f.readline()
#    line4 = f.readline()
#    line5 = f.readline()
#    line6 = f.readlines()
#    data= f.read()
#    print("Line 1", line)
#    print("Line 2", line2)
#    print("Line 3", line3)
#    print("Line 4", line4)
#    print("Line 5", line5)
#    print("Line 6", line6)
#    print("File Data", data )
   

# 3. (Read all lines into a list)
with open("file.txt", "r") as f:
    readLinesMethod = f.readlines()
    print(readLinesMethod)


# What is readlinesmethod?
# It is a method that reads all the lines of a file and returns them as a list of strings, where each string represents a line from the file.   