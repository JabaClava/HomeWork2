import random

from Graph2lists import graph2lists

#random generation graph
def ER(n, p):
    V = [i for i in range(n)]
    E = []
    for i in V:
        for j in V:
            if i != j:
                a = random.random()
                if a < p:
                    E.append([i, j])
    return graph2lists(V, E)
