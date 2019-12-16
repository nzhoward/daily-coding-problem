def print_clockwise(cntr, i, j, i_len, j_len, i_start, j_start, nums):
    
    for k in range(i_len):
        print(nums[i][j])
        cntr += 1
        if j + 1 < i_len + i_start:
            j += 1
    i += 1
    for k in range(j_len - 1):
        print(nums[i][j])
        cntr += 1
        if i + 1 < j_len + j_start:
            i += 1
    j -= 1
    for k in range(i_len - 1):
        print(nums[i][j])
        cntr += 1
        if j - 1 >= j_start:
            j -= 1
    i -= 1
    for k in range(j_len - 2):
        print(nums[i][j])
        cntr += 1
        if i - 1 >= i_start + 1:
            i -= 1
    j += 1

    if cntr == len(nums[0]) * len(nums):
        return

    print_clockwise(cntr, i, j, i_len - 2, j_len - 2, i_start + 1, j_start + 1, nums)


nums1 = [[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]

print_clockwise(0, 0, 0, len(nums1[0]), len(nums1), 0, 0, nums1)


nums2 = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9,  10, 11, 12],
         [13, 14, 15, 16]]

print_clockwise(0, 0, 0, len(nums2[0]), len(nums2), 0, 0, nums2)
