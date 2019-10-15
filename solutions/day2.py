inputList = [1, 2, 3, 4, 5]
inputList2 = [3, 2, 1]

def naive(inputList):
    product = 1
    outList = []
    for i in inputList:
        product *= i

    for i in inputList:
        outList.append(int(product / i))

    print(outList)
    return outList

assert naive(inputList) == [120, 60, 40, 30, 24]
assert naive(inputList2) == [2, 3, 6]


def noDivision(inputList):
    left = []
    for i in inputList:
        left.append(None)
    left[0] = 1
    
    for i in range(1, len(inputList)):
        left[i] = inputList[i - 1] * left[i - 1]

    right = []
    for i in inputList:
        right.append(None)
    right[-1] = 1

    for i in range(len(inputList) - 2, -1, -1):
        right[i] = inputList[i + 1] * right[i + 1]

    ans = []
    for i in range(len(inputList)):
        ans.append(left[i] * right[i])

    print(ans)
    return ans

assert noDivision(inputList) == [120, 60, 40, 30, 24]
assert noDivision(inputList2) == [2, 3, 6]
