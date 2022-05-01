from itertools import combinations 

def solution(nums):
    answer = 0
    combs = list(combinations(nums, 3))
    
    for i in combs:
        sums = sum(i)
        is_prime = True
        for j in range(2, sums // 2 + 1):
            if sums % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer

print(solution([1, 2, 7, 6, 4]))