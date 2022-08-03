def solution(priorities, location):
    answer = 0
    
    length = len(priorities)
    
    while True:
        highest = max(priorities)
        for i in range(len(priorities)):
            if highest == priorities[i]:
                answer += 1
                priorities[i] = 0
                highest = max(priorities)
                if i == location:
                    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))

# 중요도에 따라서 가장 높은 중요도보다 앞에 있는 것들은 그냥 넘어가고,
# 가장 높은 중요도인 문서를 만나면 answer에 +1 해주고 인쇄했다는 뜻으로 값을 0으로 바꿔줌.
# 이런식으로 for문을 반복해서 돌리다 보면 결국 location 위치가 0이되는 때가 오는데,
# 그 때가 내가 요청한 문서가 인쇄되는 때임