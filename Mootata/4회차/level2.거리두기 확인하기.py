from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def bfs(p, start):
    for i in start: # 각각의 응시자로부터 탐색 시작
        q = deque()
        q.append(i)
        visited = [[0 for _ in range(5)] for _ in range(5)]
        visited[i[0]][i[1]] = 1
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visited[nx][ny] != 0 or p[nx][ny] == 'X':
                    continue
                
                if p[nx][ny] == 'O':
                    q.append((nx, ny))
                    visited[nx][ny] += visited[x][y] + 1
                elif p[nx][ny] == 'P' and visited[x][y] < 3: # 탐색을 시작한 위치의 응시자로부터 거리가 2이하인 응시자가 있다면 거리두기가 지켜지지 않았다는 뜻
                    return 0
    return 1

def solution(places):
    answer = []
    
    for place in places:
        start = deque()
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P': # 응시자들의 위치
                    start.append((i, j))
        answer.append(bfs(place, start))
    
    return answer

print(solution(places))

# 각각의 응시자로부터 탐색을 시작하고 한 칸을 지날 때마다 visited +1, X는 벽이라 생각하고
# 탐색(append)하지 않음 거리(visited)가 2이하인데 다른 응시자를 만난다면 return 0
# 탐색이 끝나면 return 1

# 몰랐는데 문자열도 리스트처럼 string[1] 이런식으로 사용할 수 있음
# string = "Hello", string[1] = "e", string[4] = "o"