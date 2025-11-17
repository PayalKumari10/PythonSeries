#You are given a list of programming languages: ["Python", "Java", "C++", "Python", "Java", "C"]
#Convert it into a set and print how many unique langauges Payal knows.

programmingList= ["Python", "Java", "JS", "C++", "Python","C"]
print(type(programmingList))
#how to convert list into set

programmingSet= set(programmingList)
print(type(programmingSet))
print("Payal knows these many langauges", len(programmingSet))