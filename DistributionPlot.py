import math
import matplotlib.pyplot as plt

def distributionPlot(n, p, name):
    X = [i for i in range(n)]
    Y = []
    for x in X:
        Y.append(math.comb(n, x) * p ** x * (1 - p) ** (n - x))
    plt.loglog(X, Y, base=2, label=name)
    plt.xlabel('degree')
    plt.ylabel('count degrees')