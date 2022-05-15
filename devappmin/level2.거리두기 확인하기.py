from collections import deque

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

def sub_solution(place):
    q = deque()

    visited = [[False] * 5 for _ in range(5)]
    
    for y_idx in range(5):
        for x_idx in range(5):
            if place[y_idx][x_idx] == 'P':
                visited[y_idx][x_idx] = True 
                q.append((y_idx, x_idx))
    
    while q:
        y, x = q.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < 5 and 0 <= nx < 5):
                continue

            if place[ny][nx] == 'X':
                continue
            
            if visited[ny][nx]:
                return 0
            
            visited[ny][nx] = True

    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(sub_solution(place))

    return answer

# Test Case
test_cases = [[[
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]]]
for test_case in test_cases:
    print(solution(*test_case))