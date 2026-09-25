# Report Card Printer

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))
computer = int(input("Enter Computer Marks: "))
hindi = int(input("Enter Hindi Marks: "))

total = maths + science + english + computer + hindi
percentage = total / 5

# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Report Card
print("\n" + "="*40)
print("          REPORT CARD")
print("="*40)
print(f"Name      : {name}")
print(f"Roll No   : {roll_no}")
print("-"*40)
print(f"Maths     : {maths}")
print(f"Science   : {science}")
print(f"English   : {english}")
print(f"Computer  : {computer}")
print(f"Hindi     : {hindi}")
print("-"*40)
print(f"Total     : {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade     : {grade}")
print("="*40)