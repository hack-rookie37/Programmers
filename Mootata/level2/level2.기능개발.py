from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    progresses_q = deque(progresses)
    speeds_q = deque(speeds)
    
    while progresses_q:
        count = 0
        if progresses_q[0] < 100:
            dif = ceil((100 - progresses_q[0]) / speeds_q[0])
            for i in range(len(progresses_q)):
                progresses_q[i] += speeds_q[i] * dif
        else:
            while True:
                if progresses_q and progresses_q[0] >= 100:
                    count += 1
                    progresses_q.popleft()
                    speeds_q.popleft()
                else:
                    if count:
                        answer.append(count)
                    break
            
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 맨 앞의 작업이 끝나는데 며칠이 필요한지 계산 후 모든 작업에 각각의 진행도를 더해줌
# 맨 앞의 작업부터 진행도가 100이상인 모든 작업을 pop함
# 이후 같은 동작 반복