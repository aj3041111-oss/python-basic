def luhn(number):
    digits = [int(d) for d in str(number)]

    for i in range(len(digits)-2, -1, -2):
        digits[i] *= 2

        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    return total % 10 == 0

print(luhn("4532015112830366"))