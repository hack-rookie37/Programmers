from collections import defaultdict

def solution(topping):
    answer = 0
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    
    for i in topping:
        dic1[i] += 1
    
    for i in range(len(topping)):
        dic1[topping[i]] -= 1
        dic2[topping[i]] += 1
        if dic1[topping[i]] == 0:
            del dic1[topping[i]]
        if len(dic1) == len(dic2):
            answer += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))