from collections import defaultdict
from itertools import product

def solution(word):
    dic = defaultdict(int)
    permu = []
    for i in range(1, 6):
        for str in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            permu.append(''.join(str))
    return sorted(permu).index(word) + 1

print(solution("I"))