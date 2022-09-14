from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        dict = defaultdict(int)
        for j in orders:
            arr = sorted(list(j))
            if len(arr) >= i:
                temp = combinations(arr, i)
                for k in temp:
                    dict[k] += 1
        if dict:
            m = max(dict.values())
            for key, val in dict.items():
                if val == m and m != 1:
                    answer.append(''.join(key))
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))