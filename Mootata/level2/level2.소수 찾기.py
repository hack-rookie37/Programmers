from itertools import permutations
import math

def check(x): # 소수 판별
    if x < 2:
        return False
    for i in range (2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    permu = set()
    num = []
    for i in range(1, len(numbers) + 1):
        for j in permutations(list(numbers), i): # 주어진 숫자로 만들 수 있는 모든 조합
            permu.add(int(''.join(j))) # set으로 중복 제거
    
    for i in permu:
        if check(i):
            answer += 1
    return answer

print(solution("17"))