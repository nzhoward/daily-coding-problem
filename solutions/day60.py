def subset_same_sum(nums):
    if sum(nums) % 2 != 0:
        return False
    nums.sort()
    bag1 = []
    bag2 = []
    for i in range(len(nums)):
        if i % 2 == 0:
            bag1.append(nums[i])
        else:
            bag2.append(nums[i])
    print(bag1, bag2)
    sum1 = sum(bag1)
    sum2 = sum(bag2)
    if sum1 == sum2:
        return True
    diff = abs(sum1 - sum2)
    if sum1 > sum2 and diff / 2 in bag1:
        return True
    if sum2 > sum1 and diff / 2 in bag2:
        return True
    return False


nums1 = [15, 5, 20, 10, 35, 15, 10]
nums2 = [1, 5, 11, 5]
nums3 = [1, 5, 3]

print(subset_same_sum(nums1))
print(subset_same_sum(nums2))
print(subset_same_sum(nums3))
