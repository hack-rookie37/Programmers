from collections import defaultdict    

def solution(gems):
    l = len(gems)
    answer = [0, l - 1]
    dic = defaultdict(int)
    start, end = 0, 0
    dic[gems[start]] += 1
    kind = len(set(gems)) # 보석 종류 수
    while start < l and end < l:
        if len(dic) < kind: # 보석의 종류가 부족하면 end 증가
            end += 1
            if end == l:
                break
            dic[gems[end]] += 1
        else: # 보석의 종류수가 충분하면 start 증가
            if (end - start + 1) < (answer[1] - answer[0] + 1): # 기존의 정답보다 더 구간이 짧으면 업데이트
                answer = [start, end]
            if dic[gems[start]] == 1: # 보석의 개수가 0이 되면 딕셔너리에서 지움
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            
            start += 1
    
    answer[0] += 1 # 인덱스 0부터 시작이라 맞춰줌
    answer[1] += 1
    
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))