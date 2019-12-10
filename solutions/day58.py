def binary_search_pivot(nums, target):
    pivot = find_pivot(nums, 0, len(nums))
    if nums[pivot] == target:
        return pivot
    if nums[0] < target:
        return binary_search(nums, target, 0, pivot - 1)
    if nums[0] > target:
        return binary_search(nums, target, pivot + 1, len(nums))


def find_pivot(nums, low, high):
    mid = int((low + high) / 2)
    if nums[mid] > nums[mid + 1]:
        return mid
    elif nums[mid] < nums[mid - 1]:
        return mid - 1
    elif nums[mid] < nums[low]:
        return find_pivot(nums, low, mid - 1)
    elif nums[mid] > nums[high]:
        return find_pivot(nums, mid + 1, high)


def binary_search(nums, target, low, high):
    if high < low:
        return -1
    
    mid = int((low + high) / 2)
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return binary_search(nums, target, low, mid - 1)
    if nums[mid] < target:
        return binary_search(nums, target, mid + 1, high)


nums1 = [13, 18, 25, 2, 8, 10, 11, 12]
nums2 = [5, 6, 7, 8, 1, 2, 3]

print(binary_search_pivot(nums1, 10))
print(binary_search_pivot(nums2, 1))
