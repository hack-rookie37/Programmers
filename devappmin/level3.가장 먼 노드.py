from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    
    for node_1, node_2 in edge:
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)
        
    visited = [0] * (n + 1)
    visited[1] = 1
    
    q = deque()
    q.append(1)
    
    while q:
        parent = q.popleft()
        nodes = graph[parent]
        
        for node in nodes:
            if not visited[node]:
                visited[node] = visited[parent] + 1
                q.append(node)
    
    return sum([1 for x in visited[2:] if x == max(visited[2:])])

# Test Case
test_cases = [
                [6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]], 
            ]
test_cases_answer = [3]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")