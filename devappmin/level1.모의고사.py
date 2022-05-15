def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    match = [[0, 1], [0, 2], [0, 3]]
    
    for idx in range(len(answers)):
        number = answers[idx]
        
        if a[idx % 5] == number:
            match[0][0] += 1
        if b[idx % 8] == number:
            match[1][0] += 1
        if c[idx % 10] == number:
            match[2][0] += 1
    match.sort(key=lambda a: -a[0])
    return [name for value, name in match if value == match[0][0]]

# Test Case
test_cases = [
                [[1, 2, 3, 4, 5]], 
                [[1, 3, 2, 4, 2]],
            ]
test_cases_answer = [[1], [1, 2, 3]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")