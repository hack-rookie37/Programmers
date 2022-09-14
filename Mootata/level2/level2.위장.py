from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    
    for name, type in clothes:
        dic[type].append(name)
    
    for i in dic:
        answer *= (len(dic[i]) + 1) # 해당 타입의 의상 수 + 안입는 경우
    
    return answer - 1 # 안입는 경우가 겹쳐서 아무것도 안입는 경우가 더해지므로 -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))