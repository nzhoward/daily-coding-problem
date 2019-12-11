def fast_power(x, y):
    if y == 0:
        return 1
    half = fast_power(x, int(y / 2))
    if y % 2 == 0:
        return half * half
    else:
        return half * half * x


print(fast_power(2, 10))
print(fast_power(3, 7))
