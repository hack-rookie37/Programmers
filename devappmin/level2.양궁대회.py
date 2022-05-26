g_info = []

def sub_solution(pos, remain, info, score):
    if remain <= 0 or pos < 0:
        return score, info
    
    a_score, a_info = sub_solution(pos - 1, remain, info, score)

    new_info = [*info]
    new_info[pos] = g_info[pos] + 1
    b_score, b_info = sub_solution(pos - 1, remain - g_info[pos] - 1, new_info, score + 10 - pos + (10 - pos if g_info[pos] else 0))

    if remain - g_info[pos] - 1 >= 0:
        return (a_score, a_info) if a_score > b_score else (b_score, b_info)
    else:
        return (a_score, a_info)

def solution(n, info):
    global g_info
    g_info = info
    answer = sub_solution(10, n, [0] * 11, -sum(10 - x for x in range(len(info)) if info[x])) 
    if sum(answer[1]) != n:
        answer[1][10] += n - sum(answer[1])
    return [-1] if answer[0] <= 0 else answer[1]

# Test Case
test_cases = [
                [5, [2,1,1,1,0,0,0,0,0,0,0]],
                [1, [1,0,0,0,0,0,0,0,0,0,0]],
                [9, [0,0,1,2,0,1,1,1,1,1,1]],
                [10, [0,0,0,0,0,0,0,0,3,4,3]],
            ]
test_cases_answer = [[0,2,2,0,1,0,0,0,0,0,0], [-1], [1,1,2,0,1,2,2,0,0,0,0], [1,1,1,1,1,1,1,1,0,0,2]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")