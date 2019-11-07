def naive(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    
    max_ending_here = 0
    for i in range(len(nums)):
        ending_at_i = naive(nums[:i])
        if nums[-1] > nums[i - 1] and ending_at_i + 1 > max_ending_here:
            max_ending_here = ending_at_i + 1
    return max_ending_here


def dp(nums):
    if not nums:
        return 0
    cache = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                cache[i] = max(cache[i], cache[j] + 1)
                print(cache)
    return max(cache)


nums1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(naive(nums1))
print(dp(nums1))
