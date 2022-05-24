import re
from collections import defaultdict

def solution(s):
    nums = re.findall("((\d\,*)+)", s)
    dicts = defaultdict(int)
    
    for value, _ in nums:
        for item in value.split(','):
            dicts[item] += 1
            
    return list(map(int,[key for key in sorted(dicts, key=lambda a: -dicts[a])]))

# Test Case
test_cases = [
                ["{{2},{2,1},{2,1,3},{2,1,3,4}}"], 
                ["{{1,2,3},{2,1},{1,2,4,3},{2}}"],
                ["{{20,111},{111}}"],
                ["{{123}}"],
                ["{{4,2,3},{3},{2,3,4,1},{2,3}}"],
            ]
test_cases_answer = [[2, 1, 3, 4], [2, 1, 3, 4], [111, 20], [123], [3, 2, 4, 1]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")