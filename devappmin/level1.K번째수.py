def solution(array, commands):
    answer = []
    for fr, to, idx in commands:
        answer.append(sorted(array[fr - 1:to])[idx - 1])
    return answer

# Test Case
test_cases = [
                [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]], 
            ]
test_cases_answer = [[5, 6, 3]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")