def x(a, b):
    if a > b:
        return 0
    if a == b:
    if a < b:
        return x(a + 1, b) + x(a + 3, b)
print(x(1, 9) * x(9, 17))