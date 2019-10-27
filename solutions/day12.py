def num_ways_helper(n):
    if n <= 1:
        return n
    return num_ways_helper(n - 2) + num_ways_helper(n - 1)


def num_ways(n):
    return num_ways_helper(n + 1)


print(num_ways(4))
print(num_ways(5))


def num_ways_helper_steps(n, steps):
    if n == min(steps):
        return 1
    elif n < min(steps):
        return 0
    res = 0
    for s in steps:
        if s <= n:
            res += num_ways_helper_steps(n - s, steps)
    return res


def num_ways_steps(n, steps):
    return num_ways_helper_steps(n + 1, steps)


steps1 = {1, 3, 5}

print(num_ways_steps(4, steps1))
# 1, 1, 1, 1
# 1, 3
# 3, 1

print(num_ways_steps(5, steps1))
# 1, 1, 1, 1, 1
# 1, 3, 1
# 3, 1, 1
# 1, 1, 3
# 5

print(num_ways_steps(6, steps1))
# 1, 1, 1, 1, 1, 1
# 3, 1, 1, 1
# 1, 3, 1, 1
# 1, 1, 3, 1
# 1, 1, 1, 3
# 3, 3
# 1, 5
# 5, 1
