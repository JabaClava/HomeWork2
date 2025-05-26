def incomingDegrees(G):
    in_deg = {}
    result = {}
    for v, lst in G:
        for i in lst:
            if i in in_deg:
                in_deg[i] += 1
            else:
                in_deg[i] = 1

    for v, deg in in_deg.items():
        if deg in result:
            result[deg] += 1
        else:
            result[deg] = 1

    summ = 0
    for i, j in result.items():
        summ += j

    result[0] = 27770 - summ
    return result
