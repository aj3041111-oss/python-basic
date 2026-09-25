"""
disc_calc.py — Discount Calculator

Calculates the final price of an item after applying a discount,
and shows how much money is saved. Supports multiple items in one run.
"""


def calculate_discount(original_price: float, discount_percent: float) -> dict:
    """Return final price, amount saved, and validated inputs for a discount."""
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100.")

    savings = original_price * (discount_percent / 100)
    final_price = original_price - savings

    return {
        "original_price": round(original_price, 2),
        "discount_percent": round(discount_percent, 2),
        "savings": round(savings, 2),
        "final_price": round(final_price, 2),
    }


def prompt_float(message: str) -> float:
    while True:
        raw = input(message).strip()
        try:
            return float(raw)
        except ValueError:
            print("  Please enter a valid number.")


def main():
    print("=== Discount Calculator ===")
    print("Enter 'q' at any time to quit.\n")

    while True:
        price_raw = input("Original price: ").strip()
        if price_raw.lower() == "q":
            break

        try:
            price = float(price_raw)
        except ValueError:
            print("  Please enter a valid number.\n")
            continue

        discount_raw = input("Discount percent (e.g. 20 for 20%): ").strip()
        if discount_raw.lower() == "q":
            break

        try:
            discount = float(discount_raw)
        except ValueError:
            print("  Please enter a valid number.\n")
            continue

        try:
            result = calculate_discount(price, discount)
        except ValueError as e:
            print(f"  Error: {e}\n")
            continue

        print(
            f"  Original price : ${result['original_price']:.2f}\n"
            f"  Discount       : {result['discount_percent']:.2f}%\n"
            f"  You save       : ${result['savings']:.2f}\n"
            f"  Final price    : ${result['final_price']:.2f}\n"
        )

    print("Goodbye!")


if __name__ == "__main__":
    main()