import random

def bias_coin():
    if random.random() < 0.3:
        return 'H'
    else:
        return 'T'


def fair_coin():
    first = bias_coin()
    second = bias_coin()
    while first == second:
        first = bias_coin()
        second = bias_coin()
    return first


for i in range(10):
    print(fair_coin())
