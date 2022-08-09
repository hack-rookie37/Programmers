from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

def solution(maps):
    answer = 0
    q = deque()
    q.append((0, 0, 0))
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y, count = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return count + 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] or maps[nx][ny] == 0:
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))
    
    return -1

TC = [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]], [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]

for index, map in enumerate(TC):
    result = solution(map)
    if index == 0 and result == 11:
        print("성공", result)
    elif index == 1 and result == -1:
        print("성공", result)
    else:
        print("실패", result)