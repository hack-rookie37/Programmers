from itertools import permutations as p


def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    n = len(numbers)
    s = set()

    for i in range(1, n + 1):
        for x in p(numbers, i):
            x = int("".join(x))
            s.add(x)

    for x in s:
        if is_prime(x):
            answer += 1

    return answer
