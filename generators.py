import math

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
    seed = tab[len(tab)-1]
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
    L = math.exp(-p*amount_of_tests)
    k = 0
    p = 1
    while p > L:
        k += 1
        p *= J(0, 1, 1)[0]
    return k


def W(lambd, amount):
    tab = J(0, 1, amount)
    for x in range(amount):
        tab[x] = -math.log10(tab[x])/lambd
    return tab


def N(amount):
    tab_1 = J(0, 1, amount)
    tab_2 = J(0, 1, amount)
    for x in range(amount):
        tab_1[x] = math.sqrt(-2*math.log10(tab_1[x]))*math.cos(2*math.pi*tab_2[x])
    return tab_1