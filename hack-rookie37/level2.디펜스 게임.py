from heapq import heappush, heappop, heapify


def solution(n, k, enemy):
    R = len(enemy)
    if R <= k:
        return R

    heap = enemy[:k]
    heapify(heap)

    i = k
    while True:
        while i < R and heap[0] < enemy[i]:
            if n >= heap[0]:
                n -= heappop(heap)
            else:
                break
            heappush(heap, enemy[i])
            i += 1
        if i < R and n >= enemy[i]:
            n -= enemy[i]
            i += 1
        else:
            break

    return i
