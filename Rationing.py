#The rationing function
def rationing(slov, n):
    result = {}

    for deg, count in slov.items():
        result[deg] = count / n

    return result