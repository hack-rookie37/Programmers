from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    items = defaultdict(int)
    left, right = 0, 9
    
    for i in range(10):
        items[discount[i]] += 1
    
    while True:
        flag = True
        for i in range(len(want)):
            if items[want[i]] < number[i]: # 하나의 물품이라도 원하는 만큼 구매할 수 없다면 False
                flag = False
        if flag:
            answer += 1
        
        items[discount[left]] -= 1
        left += 1
        right += 1
        if right >= len(discount):
            break
        items[discount[right]] += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))