from itertools import combinations

def check(data): # 유일성 체크
    for i in range(len(data) - 1):
        if data[i] in data[i + 1:]:
            return False
    return True

def solution(relation):
    ck = []
    comb = []
    is_subset = False
    for i in range(1, len(relation[0]) + 1):
        comb.extend(combinations(range(len(relation[0])), i))
        
    for i in comb:
        for c in ck: # 최소성 체크
            if set(c).issubset(set(i)): # 후보키를 포함한 조합은 최소성을 만족하지 못하므로 패스
                is_subset = True
                break
        if is_subset:
            is_subset = False
            continue
        
        data = []
        for j in range(len(relation)): # 각각의 경우를 만들어서 유일성 체크
            temp = ''
            for l in i:
                temp += relation[j][l]
            data.append(temp) # ex) 'ryanmusic', 'apeachmath', 'tubecomputer', 'concomputer', 'muzimusic', 'apeachmusic'
            
        if check(data):
            ck.append(i)
    return len(ck)

print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]))