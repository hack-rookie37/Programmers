def solution(lottos, win_nums):
    match = 0
    zero = 0
    
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        for win_num in win_nums:
            if lotto == win_num:
                match += 1
    
    return sorted([min(6, 7 - match), min(6, 7 - match - zero)])

# Test Case
test_cases = [
                [[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]], 
                [[0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]],
                [[45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]]
            ]
test_cases_answer = [[3, 5], [1, 6], [1, 1]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")