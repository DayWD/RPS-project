import math
import matplotlib.pyplot as plt
from sympy.ntheory import primefactors
from sympy.ntheory.factor_ import antidivisors

# from scipy.stats import chisquare
# from statsmodels.sandbox.stats.runs import runstest_1samp

# DON'T TOUCH~~~~~~~~~
multiplier = 1597
c = 51749
m = 244944
# ~~~~~~~~~~~~~~~~~~~~

seed = 1


def G(counter):
    tab = [seed]
    for i in range(0, counter):
        tab.append((multiplier * tab[i] + c) % m)
    seed = tab[0]
    tab.pop(0)
    return tab


def J(a, b, amount):
    tab = G(amount)
    for x in range(len(tab)):
        tab[x] = (tab[x] / m) * (b - a) + a
    return tab


def B(p, amount):
    tab = J(0, 1, amount)
    for x in range(len(tab)):
        if tab[x] <= p:
            tab[x] = 1
        else:
            tab[x] = 0
    return tab


def D(p, amount_of_tests):
    tab = B(p, amount_of_tests)
    success = 0
    for x in range(len(tab)):
        if tab[x] == 1:
            success += 1
    return success

def P(p,amount_of_tests):
    L = p*amount_of_tests
    L = math.exp(-L)
    k = 0
    while p>L:
        k += 1
        p *= 1

print(G(1))
print(G(1))
print(G(1))

# asd = B(0.5,30)
# for i in asd:
#     print(i)
# P(0.5,200)

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
