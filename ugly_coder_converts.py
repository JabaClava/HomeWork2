def convert_bg2gg(graph_bad):
    graph_good = {}
    for x in graph_bad:
        graph_good[x[0]] = set(x[1])
    return graph_good