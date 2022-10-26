Q = 1234567
fibo = [0, 1] + [0] * 100000


def solution(n):

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 2] + fibo[i - 1]

    return fibo[n] % Q
