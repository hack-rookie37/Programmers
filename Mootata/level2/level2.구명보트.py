def solution(people, limit):
    answer = 0
    left, right = 0, len(people) - 1
    people.sort()
    
    while left <= right:
        answer += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
    return answer

print(solution([70, 50, 80], 100))