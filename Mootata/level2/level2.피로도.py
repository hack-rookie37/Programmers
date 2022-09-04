from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for permus in list(permutations(dungeons, len(dungeons))):
        current = k
        count = 0
        for need, use in permus:
            if need <= current:
                count += 1
                current -= use
        if count == len(dungeons):
            return count
        else:
            answer = max(answer, count)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))