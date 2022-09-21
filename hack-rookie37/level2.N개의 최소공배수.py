from functools import reduce


def gcd(x, y):
    """
    # normal
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
    """

    # Euclid
    r = x % y
    if r == 0:
        return y
    return gcd(y, r)


def lcm(x, y):
    return x * y // gcd(x, y)


def solution(arr):
    return reduce(lcm, arr)
