from collections import deque

def solution(cache_size, cities):
    cache = deque()
    work_time = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            work_time += 1
            continue
            
        cache.append(city)
        work_time += 5
        
        if len(cache) > cache_size:
            cache.popleft()
            continue
            
    return work_time

# Test Case
test_cases = [
                [3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
                [3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]],
                [2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
                [5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
                [2, ["Jeju", "Pangyo", "NewYork", "newyork"]],
                [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]
            ]
test_cases_answer = [50, 21, 60, 52, 16, 25]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
