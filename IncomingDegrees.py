#counting incoming degrees
def incomingDegrees(G):
    in_deg = {}
    result = {}

    for i in range(len(G)):
        result[i] = 0

    for v, lst in G:
        for i in lst:
            if i in in_deg:
                in_deg[i] += 1
            else:
                in_deg[i] = 1

    for v, deg in in_deg.items():
        result[deg] += 1

    summ = 0
    for i, j in result.items():
        summ += j

    result[0] = len(G) - summ
    return result
