# Budget Tracker App

balance = 0
transactions = []

while True:
    print("\n===== Budget Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: ₹"))
        balance += amount
        transactions.append(f"Income: +₹{amount}")

    elif choice == "2":
        amount = float(input("Enter expense amount: ₹"))
        balance -= amount
        transactions.append(f"Expense: -₹{amount}")

    elif choice == "3":
        print(f"\nCurrent Balance: ₹{balance:.2f}")

    elif choice == "4":
        print("\nTransaction History:")
        for t in transactions:
            print(t)

    elif choice == "5":
        print("Thank you for using Budget Tracker!")
        break

    else:
        print("Invalid choice!")