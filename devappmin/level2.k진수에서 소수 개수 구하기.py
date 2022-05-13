from math import floor

def base_change(n, k):
    answer = ""
    while n:
        n, remain = divmod(n, k)
        answer += str(remain)

    return answer[::-1]

def is_prime(num):
    if num == 1:
        return False

    for idx in range(2, floor(num ** (1 / 2)) + 1):
        if not num % idx:
            return False
    
    return True

def solution(n, k):
    answer = 0

    base_k = base_change(n, k)

    for prime_check_number in base_k.split('0'):
        if prime_check_number == '': continue

        if is_prime(int(prime_check_number)): answer += 1

    return answer

# Test Case
test_cases = [
                [437674, 3], 
                [110011, 10],
            ]
test_cases_answer = [3, 2]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")