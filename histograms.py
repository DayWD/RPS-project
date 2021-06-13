import matplotlib.pyplot as plt
import generators


def G(counter):
    tab = generators.G(counter)
    counter = int(counter / 100)
    plt.hist(tab, bins=counter)
    plt.title('Histogram of G generator')
    plt.xlabel('Generated number')
    plt.ylabel(f'Amount of numbers in one of {counter} bins')
    plt.show()


def J(a, b, amount):
    tab = generators.J(a, b, amount)
    amount = int(amount / 100)
    plt.hist(tab, bins=amount)
    plt.title('Histogram of J generator')
    plt.xlabel('Generated number')
    plt.ylabel(f'Amount of numbers in one of {amount} bins')
    plt.show()


def B(p, amount):
    tab = generators.B(p, amount)
    plt.hist(tab, bins=3)
    plt.title(f'Histogram of B generator  ( probability of success = {p} )')
    plt.xlabel('Generated number')
    plt.ylabel('Amount of numbers in interval')
    plt.show()


def D(p, amount_of_tests):
    tab = []
    for i in range(amount_of_tests):
        tab.append(generators.D(p, 10))
    amount = int(amount_of_tests / 1100)
    plt.hist(tab, bins=amount)
    plt.title(f'Histogram of D generator')
    plt.xlabel('Generated number')
    plt.ylabel(f'Amount of numbers in one of {amount} bins')
    plt.show()


def P(amount_of_tests):
    tab = []
    for i in range(amount_of_tests):
        tab.append(generators.P(4))
    amount = int(amount_of_tests / 80)
    plt.hist(tab, bins=amount)
    plt.title(f'Histogram of P generator')
    plt.xlabel('Generated number')
    plt.ylabel(f'Amount of numbers in one of {amount} bins')
    plt.show()


def W(amount):
    tab = generators.W(amount)
    amount = int(amount / 100)
    plt.hist(tab, bins=amount)
    plt.title(f'Histogram of W generator')
    plt.xlabel('Generated number')
    plt.ylabel(f'Amount of numbers in one of {amount} bins')
    plt.show()


def N(amount):
    tab = generators.N(amount)
    amount = int(amount / 100)
    plt.hist(tab, bins=amount)
    plt.title(f'Histogram of N generator')
    plt.xlabel('Generated number')
    plt.ylabel(f'Amount of numbers in one of {amount} bins')
    plt.show()
