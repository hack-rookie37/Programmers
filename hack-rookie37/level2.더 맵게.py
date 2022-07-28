import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    possible = False

    while len(scoville) > 1:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)

        if a >= K and b >= K:
            possible = True
            break

        heapq.heappush(scoville, a + (b * 2))
        answer += 1

    if len(scoville) == 1:
        if scoville[0] >= K:
            possible = True

    return answer if possible else -1
