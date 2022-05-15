from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while len(scoville) > 1:
        first, second = heappop(scoville), heappop(scoville)
        
        if first >= K:
            break
            
        answer += 1
        heappush(scoville, first + second * 2)
        
    if scoville and scoville[0] < K:
        return -1
    
    return answer

# Test Case
test_cases = [
                [[1, 2, 3, 9, 10, 12], 7]
            ]
test_cases_answer = [2]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")