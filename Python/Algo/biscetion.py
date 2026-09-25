def f(x):
    return x**3 - x - 2

def bisection(a, b, tolerance=0.0001):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2

        if f(c) == 0:
            return c

        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

root = bisection(1, 2)
print("Root =", root)