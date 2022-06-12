from collections import defaultdict, deque

def dfs(q, sheep_count,wolf_count):
    global answer
    wolf_temp = []
    answer = max(sheep_count, answer)
    
    for _ in range(len(q)):
        p = q.popleft()
        
        if infos[p] == 1:
            if sheep_count > wolf_count + 1:
                for idx in graph[p]:
                    q.append(idx)
                    
                dfs(q, sheep_count, wolf_count + 1)
                
                for idx in graph[p]:
                    q.pop()
        else:
            for idx in graph[p]:
                q.append(idx)
                
            dfs(q, sheep_count + 1, wolf_count)
            
            for idx in graph[p]:
                q.pop()
                
        q.append(p)

def solution(info, edges):
    global answer, infos, graph
    answer = 0
    infos = info
    graph = defaultdict(list)
    q = deque([0])
    
    for fr, to in edges:
        graph[fr].append(to)
        
    dfs(q, 0, 0) 
    
    return answer

# Test Case
test_cases = [
                [[0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]],
                [[0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]]
            ]
test_cases_answer = [5, 5]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
