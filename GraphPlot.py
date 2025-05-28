import matplotlib.pyplot as plt

#draw plot of all graphs
def graphPlot(in_deg, name):
    lst = list(in_deg.items())
    lst.sort()
    keys = []
    values = []
    for key, value in lst:
        keys.append(key)
        values.append(value)
    plt.loglog(keys, values, base=2, label = name, marker='o', linewidth=1, markersize=2)
    plt.xlabel('degree')
    plt.ylabel('count degrees')