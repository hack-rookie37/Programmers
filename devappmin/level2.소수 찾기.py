from itertools import permutations

def eratosfy(max_num, eratos):
    for i in range(2, max_num + 1):
        for j in range(i * i, max_num + 1, i):
            if eratos[j]:
                eratos[j] = False

def solution(numbers):
    answer = 0
    max_num = int(''.join(sorted(numbers, key=lambda a: -int(a))))
    eratos = [False, False] + [True] * (max_num - 1)
    eratosfy(max_num, eratos)
    tried = []

    for length in range(1, len(numbers) + 1):
        for item in permutations(list(numbers), length):
            combi_num = int(''.join([*item]))

            if eratos[combi_num] and combi_num not in tried:
                answer += 1
                tried.append(combi_num)

    return answer

# Test Case
test_cases = [
                ["17"], 
                ["011"],
            ]
test_cases_answer = [3, 2]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")