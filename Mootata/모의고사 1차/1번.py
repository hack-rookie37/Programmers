from collections import Counter

def solution(X, Y):
    answer = ""
    for i in sorted(list(set(X) & set(Y)), reverse = True): # 두 수의 공통된 숫자들의 목록을 구함.
        i = str(i)
        for j in range(min(X.count(i), Y.count(i))):
            answer += i
    
    if answer:
        if answer[0] == "0":
            return "0"
        else:
            return answer
    else:
        return "-1"

print(solution("12321", "42531"))