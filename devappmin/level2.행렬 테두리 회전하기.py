def move(graph, x1, y1, x2, y2):
    top = graph[y1][x1:x2]
    bottom = graph[y2][x1 + 1: x2 + 1]
    left = [graph[y][x1] for y in range(y1 + 1, y2 + 1)]
    right = [graph[y][x2] for y in range(y1, y2)]
    
    for x in range(x2 - x1):
        graph[y1][x1 + x + 1] = top[x]
        
    for y in range(y2 - y1):
        graph[y1 + y + 1][x2] = right[y]
        
    for x in range(x2 - x1):
        graph[y2][x1 + x] = bottom[x]
        
    for y in range(y2 - y1):
        graph[y1 + y][x1] = left[y]
    
    return min(*top, *bottom, *left, *right)

def solution(rows, columns, queries):
    graph = [list(range(x, x + columns)) for x in range(1, columns * rows, columns)]
    answer = []
    
    for y1, x1, y2, x2 in queries:
        answer.append(move(graph, x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    
    return answer

# Test Case
test_cases = [
                [6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]],
                [3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]],
                [100, 97, [[1,1,100,97]]],
            ]
test_cases_answer = [[8, 10, 25], [1, 1, 5, 3], [1]]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
