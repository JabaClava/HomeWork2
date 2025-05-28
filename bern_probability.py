#calculating the probability function
def bern_probability(x, n, p):
    result = 1
    q = 1 - p
    if x > n - x:
        for i in range(1, n - x + 1):
            result *= p * q / i
        for i in range(n - x + 1, x + 1):
            result *= p
        for i in range(x + 1, n + 1):
            result *= i
        return result
    for i in range(1, x + 1):
        result *= p * q / i
    for i in range(x + 1, n - x + 1):
        result *= q
    for i in range(n - x + 1, n + 1):
        result *= i
    return result
