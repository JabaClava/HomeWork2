import matplotlib.pyplot as plt

def graphPlot(in_deg, name):
    lst = list(in_deg.items())
    lst.sort()
    keys = []
    values = []
    for key, value in lst:
        keys.append(key)
        values.append(value)
    plt.loglog(keys, values, base=2, label = name)
    plt.xlabel('degree')
    plt.ylabel('count degrees')