from collections import deque

def solution(board, moves):
    moves = [x - 1 for x in moves]
    size = len(board)
    q = [deque() for _ in range(size)]
    answer = 0
    bucket = []

    for items in board:
        for item_idx in range(size):
            if items[item_idx]:
                q[item_idx].append(items[item_idx])

    for move in moves:
        if q[move]:
            item = q[move].popleft()
            if bucket and bucket[-1] == item:
                bucket.pop()
                answer += 2
                continue

            bucket.append(item)

    return answer

# Test Case
test_cases =    [
                [[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]], 
                ]
for test_case in test_cases:
    print(solution(*test_case))