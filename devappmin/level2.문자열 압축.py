
def solution(s):
    result = []

    if len(s) == 1:
        return 1
    
    for i in range(1, (len(s) // 2) + 1):
        ss = ''
        count = 1
        temp = s[:i]

        for j in range(i, len(s), i):
            if temp == s[j:i + j]:
                count += 1
                continue

            ss = ss + (str(count) if count != 1 else '') + temp
            temp = s[j:j + i]
            count = 1
        
        ss = ss + (str(count) if count != 1 else '') + temp

        result.append(len(ss))

    return min(result)



# Test Case
test_cases = [
                ["aabbaccc"], 
                ["ababcdcdababcdcd"],
                ["abcabcdede"],
                ["abcabcabcabcdededededede"],
                ["xababcdcdababcdcd"],
            ]
for test_case in test_cases:
    print(solution(*test_case))