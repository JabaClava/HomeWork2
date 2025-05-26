def graph2lists(V, E):
    G = [[i, []] for i in V]
    for v, u in E:
        G[v][1].append(u)
    return G