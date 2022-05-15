def solution(board, moves):
    answer = 0
    n = len(board[0])
    stacks = [[] for _ in range(n)]
    basket = []
    
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if board[j][i] != 0:
                stacks[i].append(board[j][i])
    
    for move in moves:
        if stacks[move - 1]:
            basket.append(stacks[move - 1].pop())
        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

# 한줄에 있는 인형의 정보를 하나의 스택에 담고, 해당 위치에서 인형을 뽑을 때 스택에서 pop
# 그 값을 basket에 담고, 마지막 값과 그 바로 앞의 값이 같다면 둘 다 지워줌