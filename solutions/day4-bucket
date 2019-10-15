# This solution takes inspriration from bucket sort. Place items in their correct place. First one out of place is the solution.

nums1 = [3, 4, -1, 1]
#    [1, 2, 3, 4]
# i = 0  1  2  3

nums2 = [1, 2, 0]
nums3 = [7, 8, 9, 11, 12]
nums4 = [1, 2, 3, 4]
nums5 = [1, 1]


def extraMemory(nums):
    n = len(nums)
    ret = [-1] * n
    for i in range(n):
        if nums[i] > 0 and nums[i] <= n:
            ret[nums[i] - 1] = nums[i]

    print(ret)
    
    for i in range(n):
        if ret[i] < 0:
            return i + 1

    return n + 1

    
print('Extra Memory')
assert extraMemory(nums1) == 2
assert extraMemory(nums2) == 3
assert extraMemory(nums3) == 1
assert extraMemory(nums4) == 5
assert extraMemory(nums5) == 2
print('######')


def constantMemory(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] > n:
            nums[i] = -1
    for i in range(n):
        while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    print(nums)

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


print('Constant Memory')
assert constantMemory(nums1) == 2
assert constantMemory(nums2) == 3
assert constantMemory(nums3) == 1
assert constantMemory(nums4) == 5
assert constantMemory(nums5) == 2
