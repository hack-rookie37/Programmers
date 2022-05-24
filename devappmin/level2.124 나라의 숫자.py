def solution(n):
    answer = ''

    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += '4'
            n = n // 3 - 1

    return answer[::-1]

# Test Case
test_cases = [
                [1],
                [2],
                [3],
                [4],
                [5],
                [6],
                [7],
                [8],
                [9],
                [10],
            ]
test_cases_answer = ['1', '2', '4', '11', '12', '14', '21', '22', '24', '41']
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")
