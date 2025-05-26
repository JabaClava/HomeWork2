
def AverageDegree(G):
    count = 0
    for v in G:
        count += sum(G[v])
    return count