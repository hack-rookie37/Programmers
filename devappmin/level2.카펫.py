def solution(brown, yellow):
    for idx in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % idx:
            continue
        
        x, y = idx, yellow // idx
        
        if brown == (y + 2) * (x + 2) - yellow:
            return [y + 2, x + 2]
    
    return []


# Test Case
test_cases = [
                [10, 2], 
                [8, 1],
                [24, 24]
            ]
test_cases_answer = [[4, 3], [3, 3], [8, 6]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")