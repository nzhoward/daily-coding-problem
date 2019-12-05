def max_sub_sum(nums):
    max_so_far = 0
    max_here = 0

    for i in range(len(nums)):
        max_here = max(nums[i], max_here + nums[i])
        max_so_far = max(max_so_far, max_here)

    return max_so_far


nums1 = [34, -50, 42, 14, -5, 86]
print(max_sub_sum(nums1))
nums2 = [-5, -1, -8, -9]
print(max_sub_sum(nums2))
nums3 = [2, 3, -7, 5, 6]
print(max_sub_sum(nums3))
