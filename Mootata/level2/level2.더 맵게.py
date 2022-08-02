from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        answer += 1
        temp1 = heappop(scoville)
        temp2 = heappop(scoville)
        heappush(scoville, temp1 + (temp2 * 2))
    if not scoville or scoville[0] < K:
        return -1
    else:
        return answer

print(solution([1, 2, 3, 9, 10, 12], 500))