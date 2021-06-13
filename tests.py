from scipy.stats import norm
import statistics
import math
import generators

def runs_test(amount_of_tests):
    tab = generators.G(amount_of_tests)
    symbols_arr = []
    mediana = statistics.median(tab)
    n = len(tab)
    n0=0
    n1=0
    for x in tab:
        if x > mediana:
            symbols_arr.append(0)
            n0 += 1
        elif x < mediana:
            symbols_arr.append(1)
            n1 += 1
    k = 1
    for i in range(1,len(symbols_arr)):
        if symbols_arr[i-1] != symbols_arr[i]:
            k += 1
    Ek = (2*n0*n1)/n + 1
    Dk = math.sqrt((2*n0*n1*(2*n0*n1-n))/((n-1)*n*n))
    Z = (k-Ek)/Dk
    print(Z)
    if norm.ppf(1 - 0.05 / 2, 0, 1) > Z > -norm.ppf(1 - 0.05 / 2, 0, 1):
        print("Test spełniony")
    else:
        print("Test nie spełniony")