from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    q = deque([0])
    
    for idx in range(n):
        if visited[idx]:
            continue
        
        answer += 1
        q.append(idx)
        visited[idx] = True
        
        while q:
            pos = q.popleft()
            
            for index, value in enumerate(computers[pos]):
                if value and not visited[index]:
                    visited[index] = True
                    q.append(index)
    
    return answer

# Test Case
test_cases = [
                [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], 
                [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]],
                [3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
            ]
test_cases_answer = [2, 1, 3]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")