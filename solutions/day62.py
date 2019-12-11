def find_ways(dp):
    n = len(dp)
    m = len(dp[0])
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    return dp[n - 1][m - 1]


n1 = 5
m1 = 5
mat1 = [[0 for i in range(n1)] for j in range(m1)]
print(find_ways(mat1))

n2 = 3
m2 = 4
mat2 = [[0 for i in range(n2)] for j in range(m2)]
print(find_ways(mat2))
