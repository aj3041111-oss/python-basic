# Movie Ticket Booking Calculator

print("===== Movie Ticket Booking =====")

movie_name = input("Enter Movie Name: ")

adult_tickets = int(input("Number of Adult Tickets: "))
child_tickets = int(input("Number of Child Tickets: "))

ADULT_PRICE = 200
CHILD_PRICE = 120

adult_cost = adult_tickets * ADULT_PRICE
child_cost = child_tickets * CHILD_PRICE

total_amount = adult_cost + child_cost

print("\n" + "="*40)
print("       MOVIE TICKET RECEIPT")
print("="*40)
print(f"Movie Name      : {movie_name}")
print(f"Adult Tickets   : {adult_tickets}")
print(f"Child Tickets   : {child_tickets}")
print(f"Adult Cost      : ₹{adult_cost}")
print(f"Child Cost      : ₹{child_cost}")
print("-"*40)
print(f"Total Amount    : ₹{total_amount}")
print("="*40)