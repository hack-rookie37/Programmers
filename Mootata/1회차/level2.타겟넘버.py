import sys
from collections import deque

input = sys.stdin.readline

numbers = list(map(int, input().split()))
target = int(input())


def bfs():
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))
    count = 0
    
    while q:
        num, index = q.popleft()
        
        if num == target and index == len(numbers) - 1:
            count += 1
        elif index < len(numbers) - 1:
            q.append((num + numbers[index + 1], index + 1))
            q.append((num - numbers[index + 1], index + 1))
    return count

print(bfs())