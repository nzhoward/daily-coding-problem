from collections import deque


def sliding_window_max(nums, k):
    dq = deque()
    res = [None] * (len(nums) + 1 - k)

    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    res[0] = nums[dq[0]]
    
    for i in range(k, len(nums)):
        print(dq)
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[i] > nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        res[i - k + 1] = nums[dq[0]]
        
    return res


nums1 = [10, 5, 2, 7, 8, 7]
k1 = 3
nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
k2 = 4
print(sliding_window_max(nums1, k1))
print(sliding_window_max(nums2, k2))
