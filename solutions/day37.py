def power_set_bit_counter(superset):
    pow_set_size = 2 ** len(superset)
    for i in range(pow_set_size):
        for j in range(len(superset)):
            if ((i & (1 << j)) > 0):
                print(superset[j], end=',')
        print('')


def power_set_recur(superset):
    subset = [None] * len(superset)
    power_set_helper(superset, subset, 0)


def power_set_helper(superset, subset, i):
    if i == len(superset):
        print_set(subset)
        print('')
    else:
        subset[i] = None
        power_set_helper(superset, subset, i + 1)
        subset[i] = superset[i]
        power_set_helper(superset, subset, i + 1)


def print_set(subset):
    for i in subset:
        if i is not None:
            print(i, end=',')


superset1 = [1, 2, 3]
power_set_bit_counter(superset1)
print('------')
power_set_recur(superset1)
