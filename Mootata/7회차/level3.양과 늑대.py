from collections import deque

def bfs(info, land):
    q = deque([[0, 1, 0, set()]])
    answer = 0
    
    while q:
        curr_node, sheep, wolves, nextnodes = q.popleft()
        answer = max(answer, sheep)
        
        for i in land[curr_node]:
            nextnodes.add(i)
        
        for i in nextnodes:
            if info[i] == 0: # 다음 노드가 양일 때
                q.append((i, sheep + 1, wolves, nextnodes - {i}))
            else: # 늑대일 때
                if sheep > wolves + 1:
                    q.append((i, sheep, wolves + 1, nextnodes - {i}))
    return answer

def solution(info, edges):
    land = [[] for _ in range(len(info))]
    
    for root, node in edges:
        land[root].append(node)
    
    print(bfs(info, land))

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])