def solution(rows, columns, queries):
    answer = []
    lists = []
    for i in range(rows):
        lists.append([j for j in range(i * columns + 1, (i + 1) * columns + 1)])
        
    for query in queries:
        x1, y1, x2, y2 = [i - 1 for i in query] # 문제의 인덱스가 1부터 시작하므로 1씩 빼줌
        temp = lists[x1][y2] # 한칸씩 옮기는 과정에서 없어지므로 저장
        min_val = temp
        
        for i in range(y2, y1, -1): # 위
            lists[x1][i] = lists[x1][i - 1]
            min_val = min(min_val, lists[x1][i - 1])
        for i in range(x1, x2): # 왼쪽
            lists[i][y1] = lists[i + 1][y1]
            min_val = min(min_val, lists[i + 1][y1])
        for i in range(y1, y2): # 아래
            lists[x2][i] = lists[x2][i + 1]
            min_val = min(min_val, lists[x2][i + 1])
        for i in range(x2, x1, -1): # 오른쪽
            lists[i][y2] = lists[i - 1][y2]
            min_val = min(min_val, lists[i - 1][y2])
        lists[x1 + 1][y2] = temp
        answer.append(min_val)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))