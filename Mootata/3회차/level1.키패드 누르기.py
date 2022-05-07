def solution(numbers, hand):
    answer = ''
    cur_left = '*'
    cur_right = '#'
    dic = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2),
           '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    
    for i in numbers:
        if i in [1, 4, 7]:
            cur_left = i
            answer += 'L'
        elif i in [3, 6, 9]:
            cur_right = i
            answer += 'R'
        else:
            temp1 = abs(dic[i][0] - dic[cur_left][0]) + abs(dic[i][1] - dic[cur_left][1])
            temp2 = abs(dic[i][0] - dic[cur_right][0]) + abs(dic[i][1] - dic[cur_right][1])
            if temp1 == temp2:
                if hand == 'left':
                    cur_left = i
                    answer += 'L'
                else:
                    cur_right = i
                    answer += 'R'
            elif temp1 < temp2:
                cur_left = i
                answer += 'L'
            else:
                cur_right = i
                answer += 'R'
            
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))