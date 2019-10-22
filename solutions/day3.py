nums_1 = [1, 2, 3, 4, 5]
nums_2 = [3, 2, 1]


def naive(nums):
    product = 1
    res = []
    for i in nums:
        product *= i

    for i in nums:
        res.append(int(product / i))

    print(res)
    return res


assert naive(nums_1) == [120, 60, 40, 30, 24]
assert naive(nums_2) == [2, 3, 6]


def no_division(nums):
    left = []
    for i in nums:
        left.append(None)
    left[0] = 1
    
    for i in range(1, len(nums)):
        left[i] = nums[i - 1] * left[i - 1]

    right = []
    for i in nums:
        right.append(None)
    right[-1] = 1

    for i in range(len(nums) - 2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]

    res = []
    for i in range(len(nums)):
        res.append(left[i] * right[i])

    print(res)
    return res


assert no_division(nums_1) == [120, 60, 40, 30, 24]
assert no_division(nums_2) == [2, 3, 6]
