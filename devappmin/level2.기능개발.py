def solution(progresses, speeds):
    answer = []
    
    while progresses:
        if progresses[0] < 100:
            progresses = [progresses[x] + speeds[x] for x in range(len(progresses))]
        else:
            count = 0
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            answer.append(count)
    return answer

# Test Case
test_cases = [
                [[93, 30, 55], [1, 30, 5]],
                [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]]
            ]
test_cases_answer = [[2, 1], [1, 3, 2]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")