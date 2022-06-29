def convert(n, number):
    v = ""
    while number:
        number, m = divmod(number, 2)
        v = v + str(m)
    return "0" * (n - len(v)) + v[::-1]

def solution(n, arr1, arr2):
    answer = [""] * n
    for idx in range(n):
        l1, l2 = convert(n, arr1[idx]), convert(n, arr2[idx])
        for i in range(n):
            answer[idx] += "#" if l1[i] == "1" or l2[i] == "1" else " "
        
    return answer

# Test Case
test_cases = [
                [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]],
                [6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]]
            ]
test_cases_answer = [
    ["#####","# # #", "### #", "#  ##", "#####"], 
    ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
