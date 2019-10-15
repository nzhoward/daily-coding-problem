inputList = [3, 4, -1, 1]
inputList2 = [1, 2, 0]
inputList3 = [2, 1]


def missingPositiveInt(inputList):
    n = len(inputList)
    if 1 not in inputList:
        return 1
    for i in range(n):
        if inputList[i] < 0 or inputList[i] > n or inputList[i] == 0:
            inputList[i] = 1

    print(inputList)

    for i in range(n):
        a = abs(inputList[i])
        if a == n:
            inputList[0] = - abs(inputList[0])
        else:
            inputList[a] = - abs(inputList[a])

    print(inputList)

    for i in range(1, n):
        if inputList[i] > 0:
            return i
    if inputList[0] > 0:
        return n

    return n + 1
        
assert missingPositiveInt(inputList) == 2
assert missingPositiveInt(inputList2) == 3
assert missingPositiveInt(inputList3) == 3
