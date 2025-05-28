import math
import matplotlib.pyplot as plt

from bern_probability import bern_probability

#plot of probability function
def distributionPlot(n, p, name):
    X = [i for i in range(n)]
    Y = []
    for x in X:
        y = bern_probability(x, n, p)
        if y < 1/n:
            y = 0
        Y.append(y)
    plt.loglog(X, Y, base=2, label=name, marker='o', linewidth=1, markersize=2)
    plt.xlabel('degree')
    plt.ylabel('count degrees')
