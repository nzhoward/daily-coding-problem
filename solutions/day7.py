def helper(num, i):
    if i > len(num) - 1:
        return 1
    if num[i] == '0':
        return 0

    res = helper(num, i + 1)
    if len(num) - i >= 2 and int(num[i: i + 2]) <= 26:
        res += helper(num, i + 2)
    return res


def num_ways(num):
    return helper(num, 0)


def helper_mem(num, i, mem):
    if i > len(num) - 1:
        return 1
    if num[i] == '0':
        return 0

    if mem[i] is not None:
        return mem[i]
    res = helper_mem(num, i + 1, mem)
    if len(num) - i >= 2 and int(num[i: i + 2]) <= 26:
        res += helper_mem(num, i + 2, mem)
    mem[i] = res
    return res


def num_ways_mem(num):
    mem = [None] * (len(num) + 1)
    return helper_mem(num, 0, mem)


print(num_ways('1234'))
print(num_ways_mem('1234'))
# 1, 2, 3, 4
# 12, 3, 4
# 1, 23, 4

print(num_ways('32145'))
print(num_ways_mem('32145'))
# 3, 2, 1, 4, 5
# 3, 21, 4, 5
# 3, 2, 14, 5

print(num_ways('12225'))
print(num_ways_mem('12225'))
# 1, 2, 2, 2, 5
# 12, 2, 2, 5
# 12, 22, 5
# 12, 2, 25
# 1, 22, 2, 5
# 1, 2, 22, 5
# 1, 2, 2, 25
# 1, 22, 25
