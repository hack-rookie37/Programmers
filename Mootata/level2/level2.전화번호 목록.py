from collections import defaultdict

def solution(phone_book):
    answer = True
    dic = defaultdict(int)
    
    for i in phone_book:
        dic[i] += 1
    
    for i in phone_book:
        prefix = ""
        
        for j in i:
            prefix += j
            if prefix in dic and prefix != i:
                return False
    
    return answer

print(solution(["119", "97674223", "1195524421"]))