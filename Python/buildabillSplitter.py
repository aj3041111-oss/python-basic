# Bill Splitter

print("===== Bill Splitter =====")

bill_amount = float(input("Enter Total Bill Amount (₹): "))
tip_percent = float(input("Enter Tip Percentage: "))
people = int(input("Enter Number of People: "))

# Calculate tip
tip_amount = (bill_amount * tip_percent) / 100

# Final bill
total_bill = bill_amount + tip_amount

# Amount per person
per_person = total_bill / people

print("\n===== Bill Summary =====")
print(f"Original Bill : ₹{bill_amount:.2f}")
print(f"Tip Amount    : ₹{tip_amount:.2f}")
print(f"Total Bill    : ₹{total_bill:.2f}")
print(f"People        : {people}")
print(f"Each Pays     : ₹{per_person:.2f}")