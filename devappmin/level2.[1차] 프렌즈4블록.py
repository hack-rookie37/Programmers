cy, cx = (0, 1, 0, 1), (0, 0, 1, 1)
answer = 0
boards = []

def play(m, n):
    global answer
    global boards
    remove = set()
    
    for y in range(m - 1):
        for x in range(n - 1):
            if boards[y][x] == '0':
                continue
            
            if len(set([boards[y + cy[idx]][x + cx[idx]] for idx in range(4)])) == 1:
                remove.update([(y + cy[idx], x + cx[idx]) for idx in range(4)])
                
    if not remove:
        return False
    
    answer += len(remove)
    boards = [[boards[y][x] for x in range(n) if (y, x) not in remove] for y in range(m)]
    
    for x in range(m):
        if len(boards[x]) < n:
            boards[x].extend(['0'] * (n - len(boards[x])))
    
    return True
    
def solution(m, n, board):
    global boards
    boards = list(zip(*[list(board[x]) for x in range(m)][::-1]))
    
    while play(n, m): pass
    
    return answer

# Test Case
test_cases = [
                [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
                [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
            ]
test_cases_answer = [14, 15]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")