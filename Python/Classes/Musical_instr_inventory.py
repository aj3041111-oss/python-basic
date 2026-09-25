inventory = {}

while True:
    print("\n===== Musical Instrument Inventory =====")
    print("1. Add Instrument")
    print("2. View Inventory")
    print("3. Search Instrument")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Instrument Name: ")
        quantity = int(input("Quantity: "))
        inventory[name] = quantity
        print("Instrument Added!")

    elif choice == "2":
        print("\nInventory:")

        if not inventory:
            print("Inventory Empty")

        for name, qty in inventory.items():
            print(f"{name} : {qty}")

    elif choice == "3":
        name = input("Enter instrument name: ")

        if name in inventory:
            print(f"{name} available: {inventory[name]}")
        else:
            print("Instrument not found")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")