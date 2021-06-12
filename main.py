import math
import matplotlib.pyplot as plt
from sympy.ntheory import primefactors
from sympy.ntheory.factor_ import antidivisors

# from scipy.stats import chisquare
# from statsmodels.sandbox.stats.runs import runstest_1samp


multiplier = 1597
c = 51749
m = 244944

# counter = 20
seed = 1


def G1(seed):
    return (multiplier * seed + c) % m


def G(counter):
    tab = [seed]
    for i in range(0, counter):
        tab.append((multiplier * tab[i] + c) % m)
    tab.pop(0)
    return tab


def J(a, b, tab):
    return (seed / m) * (b - a) + a


def B(x):
    x = J(0, 1)
    if x <= 0.5:
        return 1
    else:
        return 0


def D(counter, seed):
    score = 0
    for i in range(counter):
        seed = G(seed)
        print(B(seed))
        if B(seed) == 1:
            print(i)
            score += 1
    return score

asd = G(20)
for i in asd:
    print(i)

#   Linear congruential generator
# for i in range(counter):
#     seed = G(seed)
#     print(seed)


#   Generator J for the range from 0 to 1, but we can choose [a,b] interval
# for i in range(counter):
#     seed = G(seed)
#     print(J(0,1))


#   Coin Toss Distribution. We receive only 0 and 1 with 50% chance.
# for i in range(counter):
#     seed = G(seed)
#     print(B(seed))


#   Binomial Distribution
# attempts = 20
# asd = D(attempts, seed)
# print(asd)
