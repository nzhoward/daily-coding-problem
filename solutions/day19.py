mat1 = [[1, 2, 3, 4],
       [2, 3, 4, 5],
       [3, 4, 5, 6]]


def min_cost(costs):
    mat = [[0 for i in range(len(costs[0]))] for j in range(len(costs))]
    mat[0] = costs[0][:]
    for i in range(len(costs)):
        for j in range(len(costs[i])):
            prev = mat[i - 1][:j] + mat[i - 1][j + 1:]
            mat[i][j] = costs[i][j] + min(prev)

    print(mat)
    return min(mat[len(costs) - 1][:])
    

print(min_cost(mat1))
