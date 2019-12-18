from itertools import combinations

def count_attacks(bishops):
    cnt = 0
    for comb in combinations(bishops, 2):
        first = comb[0]
        second = comb[1]
        if abs(first[0] - second[0]) == abs(first[1] - second[1]):
            cnt += 1
    return cnt


bishops1 = [(0, 0), (1, 2), (2, 2), (4, 0)]
print(count_attacks(bishops1))
