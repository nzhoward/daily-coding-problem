import random

def rand5():
    return random.randint(1, 5)

def rand7():
    tab = [[1, 2, 3, 4, 5],
           [6, 7, 1, 2, 3],
           [4, 5, 6, 7, 1],
           [2, 3, 4, 5, 6],
           [7, 0, 0, 0, 0]]

    res = 0
    while res == 0:    
        i = rand5()
        j = rand5()
        res = tab[i - 1][j - 1]
    return res


print(rand7())
print(rand7())
print(rand7())
print(rand7())
print(rand7())
print(rand7())
