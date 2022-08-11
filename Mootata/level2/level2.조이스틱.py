from collections import defaultdict

def solution(name):
    answer = 0
    alphabets = defaultdict(int)
    min_move = len(name) - 1
    
    for i in range(1, 27):
        alphabets[chr(i + 64)] += i
    
    for i, char in enumerate(name):
        answer += min(alphabets[char] - 1, 27 - alphabets[char])
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 정방향, 연속된 A의 왼쪽 방향, 연속된 A의 오른쪽 방향 
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
        
    return answer + min_move

print(solution("AAABBAB"))