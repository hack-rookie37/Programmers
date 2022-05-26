def solution(n):
    answer = ''
    
    while n:
        cal = n % 3
        if cal: # 0이 아닐 때 
            answer += str(cal)
            n //= 3
        else: # 0일 때 (3의 배수)
            answer += '4'
            n = n // 3 - 1
    return answer[::-1]
    
print(solution(10))