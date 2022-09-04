from itertools import combinations

def solution(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer

print(solution([-3, -2, -1, 0, 1, 2, 3]))