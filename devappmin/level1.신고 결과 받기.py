from collections import defaultdict

def solution(id_list, reports, k):
    answer = []
    reports = sorted(list(set(reports)))
    dicts = defaultdict(int)
    bands = defaultdict(list)

    for report in reports:
        report = report.split()
        dicts[report[1]] += 1
        bands[report[0]].append(report[1])
    
    for id in id_list:
        val = 0
        for rp in bands[id]:
            if dicts[rp] >= k:
                val += 1

        answer.append(val)

    return answer

# Test Case
test_cases = [[["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2], [["con", "ryan"], ["ryan con","ryan con","ryan con","ryan con"], 3]]
for test_case in test_cases:
    print(solution(*test_case))
