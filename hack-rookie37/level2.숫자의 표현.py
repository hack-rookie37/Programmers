def solution(n):
    answer = 1

    left, right = 0, 1

    x = left + right

    while right < n and left < right:
        if x == n:
            answer += 1
            right += 1
            x += right - left
            left += 1
        elif x > n:
            x -= left
            left += 1
        else:
            right += 1
            x += right

    return answer
