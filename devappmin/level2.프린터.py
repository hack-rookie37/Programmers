def solution(priorities, location):
    answer_location = [False] * len(priorities)
    answer_location[location] = True
    answer = 1
    
    while priorities:
        if [x for x in priorities[1:] if priorities[0] < x]:
            priorities.append(priorities.pop(0))
            answer_location.append(answer_location.pop(0))
        else:
            priorities.pop(0)
            if answer_location.pop(0): break
            answer += 1
    
    return answer

# Test Case
test_cases = [
                [[2, 1, 3, 2], 2],
                [[1, 1, 9, 1, 1, 1], 0],
            ]
test_cases_answer = [1, 5]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")