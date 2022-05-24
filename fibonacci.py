def fibonacci(n):
    """
    Return nth Fibonacci number, for positive `n`.

    :param n: Takes positive integer number
    :return: nth fibonacci series
    """
    n_minus1, n_minus2 = 1, 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result
        return result


for i in range(36):
    print(i, fibonacci(i))


