nums_1 = [3, 4, -1, 1]
nums_2 = [1, 2, 0]
nums_3 = [2, 1]


def missing_positive_int(nums):
    n = len(nums)
    if 1 not in nums:
        return 1
    for i in range(n):
        if nums[i] < 0 or nums[i] > n or nums[i] == 0:
            nums[i] = 1

    print(nums)

    for i in range(n):
        a = abs(nums[i])
        if a == n:
            nums[0] = - abs(nums[0])
        else:
            nums[a] = - abs(nums[a])

    print(nums)

    for i in range(1, n):
        if nums[i] > 0:
            return i
    if nums[0] > 0:
        return n

    return n + 1


assert missing_positive_int(nums_1) == 2
assert missing_positive_int(nums_2) == 3
assert missing_positive_int(nums_3) == 3
