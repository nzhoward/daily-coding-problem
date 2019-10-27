def max_sum(nums):
    incl = nums[0]
    excl = 0

    for i in range(1, len(nums)):
        excl_new = max(incl, excl)
        incl = excl + nums[i]
        excl = excl_new
        
    return max(incl, excl)


nums1 = [2, 4, 6, 2, 5]
nums2 = [5, 1, 1, 5]
print(max_sum(nums1))
print(max_sum(nums2))
