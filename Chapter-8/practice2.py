# Open a file called report.txt in write mode.

# file= open("report.txt", "w", encoding="utf-8")

#write in append mode
file= open("report.txt", "a", encoding="utf-8")
file.write("All Set")

file.write("Kafi sahi se Python Sikh rahe hai. Maja aaraha hai \n")
file.write("File handling bhi seekh liya hai. \n")
file.write("Ab hum practice karenge. \n")