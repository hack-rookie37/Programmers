from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

def solution(maps):
    q = deque([(0, 0)])
    my, mx = len(maps), len(maps[0])
    visited = [[0] * mx for _ in range(my)]
    visited[0][0] = 1
    
    while q:
        y, x = q.popleft()
        
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            
            if not (0 <= ny < my and 0 <= nx < mx):
                continue 
                
            if visited[ny][nx]:
                continue
            
            if not maps[ny][nx]:
                continue
                
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))
            
    return visited[my - 1][mx - 1] if visited[my - 1][mx - 1] else -1

# Test Case
test_cases = [
                [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]],
                [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]
            ]
test_cases_answer = [11, -1]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
