
def average_degree(G):
    count = 0
    for v in G:
        count += len(G[v])
    return count / len(G)