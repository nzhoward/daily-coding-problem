def smallest_interval(nums):
    k = [0] * len(nums)
    interval = [float('-inf'), float('inf')]

    while True:
        min_idx = -1
        end = False
        local_max = float('-inf')
        local_min = float('inf')
        
        for i in range(len(k)):
            if k[i] >= len(nums[i]):
                end = True
                break
            if nums[i][k[i]] > local_max:
                local_max = nums[i][k[i]]
            if nums[i][k[i]] < local_min:
                local_min = nums[i][k[i]]
                min_idx = i

        if end:
            break
            
        if local_max - local_min < interval[1] - interval[0]:
            interval[0] = local_min
            interval[1] = local_max

        k[min_idx] += 1

    return interval


a = [0, 1, 4, 17, 20, 25, 31]
b = [5, 6, 10]
c = [0, 3, 7, 8, 12]
nums = [a, b, c]

print(smallest_interval(nums))
assert smallest_interval(nums) == [3, 5]
