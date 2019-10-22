nums_1 = [10, 15, 3, 7]
k1 = 17
k2 = 20


def naive(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False


assert naive(nums_1, k1)
assert not naive(nums_1, k2)


def one_pass(nums, k):
    val = {}
    for i in range(k + 1):
        val[i] = False

    for i in nums:
        if val[k - i]:
            return True
        elif val[i] == 0:
            val[i] = True

    return False


assert one_pass(nums_1, k1)
assert not one_pass(nums_1, k2)
