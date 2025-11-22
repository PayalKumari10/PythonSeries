# Expense Tracker Project

expensesList = []  # list of all expenses

print("Welcome to Expense Tracker! Thoda smart kharcha, zyada savings.")

while True:
    print("\n==== Menu ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # 1. ADD EXPENSE
    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (e.g., Food, Transport, Shopping): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nExpense added successfully!")

    # 2. VIEW ALL EXPENSES
    elif choice == "2":
        if len(expensesList) == 0:
            print("\nNo expenses recorded yet.")
        else:
            print("\n=== All Expenses ===")
            count = 1
            for e in expensesList:
                print(f"{count}. {e['date']} | {e['category']} | {e['description']} | {e['amount']}")
                count += 1

    # 3. VIEW TOTAL
    elif choice == "3":
        total = 0
        for e in expensesList:
            total += e["amount"]
        print("\nTotal Expenses =", total)

    # 4. EXIT
    elif choice == "4":
        print("\nExiting Expense Tracker. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
