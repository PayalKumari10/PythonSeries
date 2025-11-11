#billcalculater
Total_bill = float(input("Enter the total bill amout"))
Tip_percentage = float(input("Enter the tip percentage you want to give: "))
Tip_amount = (Tip_percentage / 100) * Total_bill
Final_amount = Total_bill + Tip_amount
print("The final amount to be paid is: ", Final_amount)
print("The tip amount is: ", Tip_amount)
print("Each will pay: " , Final_amount / 2)


