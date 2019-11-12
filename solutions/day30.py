def trap_water(nums):
    end = False
    idx = 0
    ans = 0
    while not end:
        if idx == len(nums) - 1:
            end = True
            continue
        left_idx = idx
        left_height = nums[idx]
        while nums[idx + 1] < left_height:
            idx += 1
            if idx == len(nums) - 1:
                end = True
                break
        if not end:
            right_idx = idx + 1
            right_height = nums[idx + 1]
            trap_height = min(left_height, right_height)
            for i in range(left_idx + 1, right_idx):
                ans += trap_height - nums[i]
            idx = right_idx
    return ans


nums1 = [2, 1, 2]
nums2 = [3, 0, 1, 3, 0, 5]
nums3 = [4, 2, 1, 6]
nums4 = [1, 2, 1]
nums5 = [0, 0, 0, 0]

print(trap_water(nums1))
print(trap_water(nums2))
print(trap_water(nums3))
print(trap_water(nums4))
print(trap_water(nums5))
