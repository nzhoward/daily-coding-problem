# This solution takes inspriration from bucket sort. Place items in their correct place. First one out of place is the solution.

nums1 = [3, 4, -1, 1]
#    [1, 2, 3, 4]
# i = 0  1  2  3

nums2 = [1, 2, 0]
nums3 = [7, 8, 9, 11, 12]
nums4 = [1, 2, 3, 4]
nums5 = [1, 1]


def extra_mem(nums):
    n = len(nums)
    ret = [-1] * n
    for i in range(n):
        if 0 < nums[i] <= n:
            ret[nums[i] - 1] = nums[i]

    print(ret)

    for i in range(n):
        if ret[i] < 0:
            return i + 1

    return n + 1


print('Extra Memory')
assert extra_mem(nums1) == 2
assert extra_mem(nums2) == 3
assert extra_mem(nums3) == 1
assert extra_mem(nums4) == 5
assert extra_mem(nums5) == 2
print('######')


def constant_mem(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] > n:
            nums[i] = -1
    for i in range(n):
        while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    print(nums)

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


print('Constant Memory')
assert constant_mem(nums1) == 2
assert constant_mem(nums2) == 3
assert constant_mem(nums3) == 1
assert constant_mem(nums4) == 5
assert constant_mem(nums5) == 2
