def is_prime(x):
    if x <= 1:
        return 0

    if x == 2:
        return 1

    for i in range(3, int(x ** (1 / 2) + 1)):
        if x % i == 0:
            return 0

    return 1


def solution(n, k):
    answer = 0
    m = []
    while n:
        m.append(str(n % k))
        n //= k

    m = "".join(reversed(m))

    for x in filter(lambda x: x != "", m.split("0")):
        if is_prime(int(x)):
            answer += 1

    return answer
