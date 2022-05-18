from itertools import combinations

def solution(relation):
    zipped = [x for x in zip(*relation)]
    visited = []
    answer = 0
    
    for idx in range(1, len(relation[0]) + 1):
        for item in combinations(range(len(relation[0])), idx):
            already = False
            for v in visited:
                if all(i in item for i in v):
                    already = True
                    break
            if already: continue
                
            combined = [x for x in zip(*[zipped[x] for x in item])]
            if len(combined) == len(set(combined)):
                visited.append(item)
                answer += 1
    
    return answer

# Test Case
test_cases = [
    [[ 
        ["100","ryan","music","2"],
        ["200","apeach","math","2"],
        ["300","tube","computer","3"],
        ["400","con","computer","4"],
        ["500","muzi","music","3"],
        ["600","apeach","music","2"]
    ]],
    [[["1"], ["2"], ["3"], ["4"]]],
    [[
        ["100", "ryan", "music", "2", "gogo"], 
        ["200", "apeach", "math", "2", "gogo"], 
        ["300", "tube", "computer", "3", "gogo"], 
        ["400", "con", "computer", "4", "gogo"], 
        ["500", "muzi", "music", "3", "gogo"], 
        ["600", "apeach", "music", "2", "gogo"]
    ]],
    [[
        ["100", "ryan", "music", "2"], 
        ["200", "apeach", "math", "2"], 
        ["300", "tube", "computer", "3"], 
        ["400", "con", "computer", "4"], 
        ["500", "muzi", "music", "3"], 
        ["600", "apeach", "music", "1"]
    ]],
    ]
test_cases_answer = [2, 1, 2, 4]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")