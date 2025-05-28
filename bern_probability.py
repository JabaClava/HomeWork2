def bern_probability(x, n, p):
    result = 1
    if x > n - x:
        for i in range(n - x + 1):
            result *= p * (1 - p) / i
        for i in range(n - x + 1, x + 1):
            result *= p * (1 - p)
        for i in range(x + 1, n + 1):
            result *= i
        return result
    for i in range(x + 1):
        result *= p * (1 - p) / i
    for i in range(n - x + 1, n + 1):
        result *= i
    return result
