def max_returns(prices):
    max_prof = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            tmp = prices[j] - prices[i]
            if tmp > max_prof:
                max_prof = tmp

    return max_prof


def max_returns_onepass(prices):
    max_prof = 0
    min_price = float('inf')
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_prof:
            max_prof = prices[i] - min_price

    return max_prof


prices1 = [9, 11, 8, 5, 7, 10]
print(max_returns(prices1))
print(max_returns_onepass(prices1))

prices2 = [100, 3, 2, 1, 10]
print(max_returns(prices2))
print(max_returns_onepass(prices2))
