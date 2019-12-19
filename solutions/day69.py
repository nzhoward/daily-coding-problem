def largest_product(nums):
    nums = sorted(nums, key=abs)
    print(nums)
    n = len(nums) - 1
    max_vals = [nums[n], nums[n - 1], nums[n - 2]]
    while get_prod(max_vals) < 0 and n - 2 > 0:
        n -= 1
        max_vals[2] = nums[n - 2]
    min_vals = [nums[0], nums[1], nums[2]]
    return max(get_prod(max_vals), get_prod(min_vals))


def get_prod(nums):
    ret = 1
    for i in nums:
        ret *= i
    return ret



nums1 = [-10, -10, 5, 2]
nums2 = [1, -4, 3, -6, 7, 0]
nums3 = [-10, -3, -5, -6, -20]

print(largest_product(nums1))
print(largest_product(nums2))
print(largest_product(nums3))
