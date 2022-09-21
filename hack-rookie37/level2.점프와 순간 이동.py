def solution(n):
    ans = 0

    while n > 0:
        while not n % 2:
            n /= 2
        n -= 1
        ans += 1

    return ans
