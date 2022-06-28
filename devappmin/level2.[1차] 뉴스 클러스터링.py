from collections import defaultdict
from math import floor
import re

def solution(str1, str2):
    o_dicts, t_dicts = defaultdict(int), defaultdict(int)
    o_sets, t_sets = set(), set()
    
    for pm in range(len(str1) - 1):
        pmt = "".join([str1[pm], str1[pm + 1]]).lower()
        if re.fullmatch(r'[a-z]*', pmt):
            o_dicts[pmt] += 1
            o_sets.add(pmt)
            
    for pm in range(len(str2) - 1):
        pmt = "".join([str2[pm], str2[pm + 1]]).lower()
        if re.fullmatch(r'[a-z]*', pmt):
            t_dicts[pmt] += 1
            t_sets.add(pmt)
            
    intersection = o_sets | t_sets
    union = o_sets & t_sets
    ic, uc = 0, 0
    
    for item in intersection:
        ic += max(o_dicts[item], t_dicts[item])
    
    for item in union:
        uc += min(o_dicts[item], t_dicts[item])
        
    if not ic and not uc:
        return 65536
    
    return floor(uc / ic * 65536)

# Test Case
test_cases = [
                [ "FRANCE", "french" ],
                [ "handshake", "shake hands" ],
                [ "aa1+aa2", "AAAA12" ],
                [ "E=M*C^2", "e=m*c^2" ]
            ]
test_cases_answer = [16384, 65536, 43690, 65536]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
