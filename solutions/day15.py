import random

count = 0


def get_uniform(x):
    global count
    res = None
    count += 1
    if count == 1:
        res = x
    else:
        tmp = random.randrange(count)
        if tmp == count - 1:
            res = x
    return res


stream = [1, 3, 2, 5, 2, 6, 4, 3]
for i in stream:
    print(get_uniform(i))

print('Count:', count)
