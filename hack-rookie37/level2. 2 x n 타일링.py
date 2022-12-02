Q = int("1,000,000,007".replace(",", ""))


def solution(n):
    dp = [0, 1, 2] + [0] * (n - 2)

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % Q

    return dp[n]
