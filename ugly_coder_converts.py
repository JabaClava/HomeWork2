def convert_bg2gg(graph_bad):
    graph_good = {}
    for x in graph_bad:
        graph_good[x[0]] = set(x[1])
    return graph_good

def convert_gg2bg(graph_good):
    graph_bad = []
    for key, val in graph_good.items():
        graph_bad.append([key, val])
    return graph_bad