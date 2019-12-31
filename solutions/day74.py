def find_mult(N, X):
    ret = 0
    for i in range(1, N + 1):
        if X / i > N or X % i != 0:
            continue
        ret += 1
    return ret


print(find_mult(6, 12))
print(find_mult(6, 16))
print(find_mult(6, 18))
print(find_mult(8, 16))
print(find_mult(9, 18))
