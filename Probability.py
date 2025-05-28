def probability(G):
    count = 0
    for v, lst in G:
        count += len(lst)
    return count / len(G) ** 2