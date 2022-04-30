from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(infos, queries):
    answer = []
    dicts = defaultdict(list)

    for info in infos:
        info = info.split()
        people = info[:-1]
        score = int(info[-1])

        for idx in range(5):
            for case in combinations(people, idx):
                dicts[''.join(case)].append(score)
    
    for value in dicts.values():
        value.sort()

    for query in queries:
        query = query.replace("and ", "").replace("-", "").split()

        key = ''.join(query[:-1])
        score = int(query[-1])
        answer.append(len(dicts[key]) - bisect_left(dicts[key], score))

    return answer


def solution_time_out(infos, queries):
    answer = []

    for query in queries:
        query = query.replace("and ", "")

        # lang, position, lvl, food, score
        query = list(query.split())

        ans = 0
        for info in infos:
            info = list(info.split())

            match = True
            for idx in range(4):
                if not (query[idx] == info[idx] or query[idx] == "-"):
                    match = False
                    break
                
            if match and int(query[4]) <= int(info[4]):
                ans += 1

        answer.append(ans)

    return answer


# Test Case
test_cases =    [
                [["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], 
                ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]]
                ]
for test_case in test_cases:
    print(solution(*test_case))