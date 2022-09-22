def solution(arr1, arr2):
    m, n, x = len(arr1), len(arr2[0]), len(arr2)
    answer = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(x):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer
