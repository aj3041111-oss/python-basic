def apply_discount(price, discount_percent):
    discount_amount = (price * discount_percent) / 100
    final_price = price - discount_amount
    return final_price

# Example
price = float(input("Enter Product Price: "))
discount = float(input("Enter Discount Percentage: "))

result = apply_discount(price, discount)

print("Final Price =", result)