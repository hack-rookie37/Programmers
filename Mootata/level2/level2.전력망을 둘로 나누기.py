from collections import deque
from itertools import permutations

def bfs(dl1, dl2, elecs, visited):
    q = deque()
    q.append(dl1)
    count = 0
    
    while q:
        v = q.popleft()
        for k in elecs[v]:
            if k == dl2 or visited[k]: # dl1, dl2의 연결을 끊음.
                continue
            q.append(k)
        visited[v] = True
        count += 1
    return count

def solution(n, wires):
    answer = float('inf')
    elecs = [[] for _ in range(n + 1)]
    
    count = 0
    
    for v1, v2 in wires:
        elecs[v1].append(v2)
        elecs[v2].append(v1)
    
    for v1, v2 in wires:
        visited = [False for _ in range(n + 1)]
        count = bfs(v1, v2, elecs, visited)
        answer = min(answer, abs(n - (count * 2)))
        if not answer:
            return answer
        
    return answer

print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))