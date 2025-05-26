# ------
def average_in_degs(arr_in_degs):
    N = len(arr_in_degs)
    keys = set()
    result = {}
    for in_degs in arr_in_degs:
        keys |= in_degs.keys()
    for key in keys:
        result[key] = 0
        for in_degs in arr_in_degs:
            result[key] += in_degs.get(key, 0)
        result[key] /= N
    return result