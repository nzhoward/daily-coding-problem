import heapq

def running_median(nums):
    min_heap = []
    max_heap = []
    for i in range(len(nums)):
        if i == 0:
            heapq.heappush(min_heap, nums[i])
        elif nums[i] <= min_heap[0]:
            heapq.heappush(max_heap, -nums[i])
        elif nums[i] > min_heap[0]:
            heapq.heappush(min_heap, nums[i])

        if abs(len(min_heap) - len(max_heap)) > 1:
            balance(max_heap, min_heap)

        if len(max_heap) == len(min_heap):
            med = (min_heap[0] - max_heap[0]) / 2
            if med.is_integer():
                print(int(med))
            else:    
                print(med)
        elif len(max_heap) < len(min_heap):
            print(min_heap[0])
        elif len(min_heap) < len(max_heap):
            print(-max_heap[0])


def balance(max_heap, min_heap):
    if len(max_heap) - len(min_heap) > 1:
        heapq.heappush(min_heap, -max_heap[0])
        heapq.heappop(max_heap)
    elif len(min_heap) - len(max_heap) > 1:
        heapq.heappush(max_heap, -min_heap[0])
        heapq.heappop(min_heap)


nums1 = [2, 1, 5, 7, 2, 0, 5]
running_median(nums1)

print('---')
nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
running_median(nums2)

print('---')
nums3 = [4, 4, 2, 2, 5, 1, 7]
running_median(nums3)

print('---')
nums4 = [0, 0, 0, 0]
running_median(nums4)
