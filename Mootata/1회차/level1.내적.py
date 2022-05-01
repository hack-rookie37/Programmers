a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

print(solution(a, b))