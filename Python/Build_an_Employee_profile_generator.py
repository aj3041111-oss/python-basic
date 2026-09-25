# Employee Profile Generator

print("===== Employee Profile Generator =====")

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
designation = input("Enter Designation: ")
salary = float(input("Enter Salary: "))
experience = int(input("Enter Years of Experience: "))

# Bonus Calculation
if experience >= 10:
    bonus = salary * 0.20
elif experience >= 5:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

total_salary = salary + bonus

# Employee Profile
print("\n" + "="*40)
print("       EMPLOYEE PROFILE")
print("="*40)
print(f"Name        : {name}")
print(f"Employee ID : {emp_id}")
print(f"Department  : {department}")
print(f"Designation : {designation}")
print(f"Salary      : ₹{salary:,.2f}")
print(f"Experience  : {experience} years")
print(f"Bonus       : ₹{bonus:,.2f}")
print(f"Total Pay   : ₹{total_salary:,.2f}")
print("="*40)