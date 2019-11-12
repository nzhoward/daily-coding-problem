def edit_distance(first, second):
    m = len(first)
    n = len(second)
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1)
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]
    

first1 = 'kitten'
second1 = 'sitting'
print(edit_distance(first1, second1))

first2 = 'cat'
second2 = 'dog'
print(edit_distance(first2, second2))

first3 = 'cat'
second3 = 'cat'
print(edit_distance(first3, second3))

first4 = 'alongword'
second4 = 'anevenlongerword'
print(edit_distance(first4, second4))
