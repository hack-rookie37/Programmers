from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

infos = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
queries = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
answer = []
dic = defaultdict(list)

for info in infos:
    info = info.split()
    condition = info[:-1] # 점수를 제외한 조건들
    score = int(info[-1]) # 점수
    
    for i in range(5): # '-' 가 들어간 것을 포함한 모든 경우
        case = list(combinations([0,1,2,3], i))
        
        for c in case:
            tmp = condition.copy()
            
            for idx in c:
                tmp[idx] = "-"
            
            key = ''.join(tmp)
            dic[key].append(score) # 조건이 키, 점수가 밸류인 딕셔너리

for value in dic.values(): # 이분탐색을 위해서 정렬
    value.sort()   

for query in queries:
    query = query.replace("and ", "").split()
    key = ''.join(query[:-1]) # 조건
    score = int(query[-1]) # 점수
    count = 0
    
    if key in dic:
        target = dic[key] # 조건에 맞는 것들의 점수를 가져옴
        idx = bisect_left(target, score) # bisect_left를 이용해 조건 이상의 점수를 찾음
        count = len(target) - idx
    
    answer.append(count)  

print(answer)