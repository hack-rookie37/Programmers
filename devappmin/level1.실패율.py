from collections import defaultdict

def solution(N, stages):
    clear = [0] * (N + 1)
    total_people = len(stages)
    
    for stage in range(1, N + 1):
        new_stages = []
        for person in stages:
            if person <= stage:
                clear[stage] += 1
                continue
            
            new_stages.append(person)
        stages = new_stages
        
    answer = []
    
    for level, failed in enumerate(clear):
        if not level: continue
        
        if not total_people:
            answer.append((level, 0))
            continue
            
        answer.append((level, failed / total_people))
        total_people -= failed
    
    answer = sorted(answer, key=lambda a: (-a[1], a[0]))
    
    
    return [x for x, _ in answer]

# Test Case
test_cases = [
                [5, [2, 1, 2, 6, 2, 4, 3, 3]], 
                [4, [4, 4, 4, 4, 4]]
            ]
test_cases_answer = [[3,4,2,1,5], [4,1,2,3]]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
