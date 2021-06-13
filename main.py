import math
import statistics
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
    global seed
    tab = [seed]
    for i in range(0, counter):
        tab.append((multiplier * tab[i] + c) % m)
    seed = tab[len(tab) - 1]
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


def P(p, amount_of_tests):
    L = math.exp(-p * amount_of_tests)
    k = 0
    p = 1
    while p > L:
        k += 1
        p *= J(0, 1, 1)[0]
    return k


def W(lambd, amount):
    tab = J(0, 1, amount)
    for x in range(amount):
        tab[x] = -math.log10(tab[x]) / lambd
    return tab


def N(amount):
    tab_1 = J(0, 1, amount)
    tab_2 = J(0, 1, amount)
    for x in range(amount):
        tab_1[x] = math.sqrt(-2 * math.log10(tab_1[x])) * math.cos(2 * math.pi * tab_2[x])
    return tab_1


def runs_test(amount_of_tests):
    tab = G(amount_of_tests)
    symbols_arr = []
    mediana = statistics.median(tab)
    n = len(tab)
    n0 = 0
    n1 = 0
    for x in tab:
        if x > mediana:
            symbols_arr.append(0)
            n0 += 1
        elif x < mediana:
            symbols_arr.append(1)
            n1 += 1
    k = 1
    for i in range(1, len(symbols_arr)):
        if symbols_arr[i - 1] != symbols_arr[i]:
            k += 1
    Ek = (2 * n0 * n1) / n + 1
    Dk = math.sqrt((2 * n0 * n1 * (2 * n0 * n1 - n)) / ((n - 1) * n * n))
    Z = (k - Ek) / Dk
    return Z

# asd = G(15)
# for i in asd:
#     print(i)

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
