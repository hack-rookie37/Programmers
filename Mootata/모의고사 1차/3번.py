from collections import deque

def solution(order):
    answer = 0
    belt = deque([i for i in range(1, len(order) + 1)])
    stack = []
    
    for i in order:
        while True:
            if belt and belt[0] == i: # 메인 벨트에서 꺼낸 박스가 순서와 맞을 때
                belt.popleft()
                answer += 1
                break
            else: # 메인 벨트가 비어있거나, 박스가 순서와 다를 때
                if stack and stack[-1] == i: # 보조 벨트의 박스가 순서와 맞을 때
                    stack.pop()
                    answer += 1
                    break
                elif belt: # 보조 벨트의 박스가 순서와 다르지만 메인 벨트가 비어있지는 않을 때
                    stack.append(belt.popleft())
                else: # 메인 벨트가 비어있고, 보조 벨트의 박스도 순서와 다를 때
                    return answer
    return answer

print(solution([4,3,1,2,5]))