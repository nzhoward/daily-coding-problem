inputList = [10, 15, 3, 7]
k = 17
k2 = 20

def naive(inputList, inputK):
    for i in range(len(inputList)):
        for j in range(i + 1, len(inputList)):
            if inputList[i] + inputList[j] == inputK:
                return True;
    return False;


assert naive(inputList, k) == True
assert naive(inputList, k2) == False


def onePass(inputList, inputK):
    val = {}
    for i in range(inputK + 1):
        val[i] = False

    for i in inputList:
        if val[inputK - i] == True:
            return True
        elif val[i] == 0:
            val[i] = True

    return False


assert onePass(inputList, k) == True
assert onePass(inputList, k2) == False
