def rationing(slov):
    result = {}

    for deg, count in slov.items():
        result[deg] = count / 27770

    return result