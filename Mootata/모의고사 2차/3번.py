from heapq import heappop, heappush

def solution(n, roads, sources, destination):
    answer = []
    hq = []
    locations = [[] for _ in range(n + 1)]
    weights = [float('inf') for _ in range(n + 1)]
    for x, y in roads:
        locations[x].append((1, y))
        locations[y].append((1, x))
    heappush(hq, (0, destination))
    weights[destination] = 0
    
    while hq:
        weight, v = heappop(hq)
        
        if weights[v] < weight:
            continue
        
        for w, node in locations[v]:
            next_weight = weight + w
            if weights[node] > next_weight:
                heappush(hq, (next_weight, node))
                weights[node] = next_weight
    
    for i in sources:
        a = weights[i]
        if a < float('inf'):
            answer.append(a)
        else:
            answer.append(-1)
    return answer

print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))