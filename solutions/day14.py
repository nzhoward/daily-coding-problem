import random


def estimate_pi_monte_carlo():
    inside = 0
    outside = 0

    for i in range(1000000):
        a = random.uniform(-1, 1)
        b = random.uniform(-1, 1)
        if a**2 + b**2 <= 1:
            inside += 1
        else:
            outside += 1

    return 4 * inside / (inside + outside)


print(estimate_pi_monte_carlo())
