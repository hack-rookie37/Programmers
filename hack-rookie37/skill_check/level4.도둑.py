# 인접한 집은 털면 안된다.
# money 배열에 집이 갖고있는 돈 들어있음
# 원형 집이라 첫번째 집과 마지막집이 인접해있음


def solution(money):

    house = len(money)
    dp = [[0] * 2 for _ in range(house)]

    dp[0][0] = money[0]
    dp[0][1] = 0

    dp[1][0] = max(dp[0])
    dp[1][1] = money[1]

    for i in range(2, house):
        dp[i][0] = max(dp[i - 2][0] + money[i], dp[i - 1][0])
        dp[i][1] = max(dp[i - 2][1] + money[i], dp[i - 1][1])

    return max(dp[-1][1], max(dp[-2]))
