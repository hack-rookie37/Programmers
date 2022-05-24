from collections import deque

def bfs(n, info):
    q = deque()
    q.append((0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    count = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gap = 0
    
    while q:
        score, arrow = q.popleft() # 현재 화살을 쏠 과녁 점수, 쏜 화살 현황
        
        if sum(arrow) < n: # 아직 화살이 남았을 때
            if score == 10: # 마지막 과녁에 쏠 차례지만 화살이 남았을 때
                temp = arrow[:]
                temp[score] = n - sum(arrow) # 남은 화살을 모두 맞춤
                q.append((score + 1, temp))
            else:
                temp = arrow[:] # 어피치보다 한발 더 맞춤
                temp[score] = info[score] + 1
                if sum(temp) <= n: # 어피치보다 한발 더 쐈을 때 화살의 총개수인 n을 넘지 않아야 함
                    q.append((score + 1, temp))
                temp2 = arrow[:] # 화살을 쏘지 않고 넘어감
                temp2[score] = 0
                q.append((score + 1, temp2))
                    
        else: # 화살을 모두 쐈을 때
            apeach, lion = 0, 0
            
            for i in range(11):
                if info[i] >= arrow[i] and info[i] != 0: # 라이언보다 많이 맞춘 경우에 해당 점수를 더해줌
                    apeach += 10 - i
                elif arrow[i] != 0: # 어피치보다 많이 맞춘 경우만 있기 때문에 0이 아니라면 해당 점수를 더해줌
                    lion += 10 - i
                    
            temp_gap = lion - apeach # 점수 차이
            
            if lion > apeach:
                if gap < temp_gap:
                    gap = temp_gap
                    result = arrow[:]
                elif gap == temp_gap: # 점수 차이가 같다면
                    for i in range(10, -1, -1): # 더 낮은 점수를 많이 맞춘 경우를 선택
                        if arrow[i] > result[i]:
                            result = arrow[:]
                            break
    return result


def solution(n, info):
    answer = bfs(n, info)
    if sum(answer) == 0:
        print(-1)
    else:
        print(answer)

TC = [(5, [2,1,1,1,0,0,0,0,0,0,0]), (1, [1,0,0,0,0,0,0,0,0,0,0]), (9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]), (10, [0,0,0,0,0,0,0,0,3,4,3])]

for n, info in TC:
    solution(n, info)