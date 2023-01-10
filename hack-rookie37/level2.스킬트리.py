from collections import deque


def solution(skill, skill_trees):
    answer = 0

    skill = list(skill)
    for s_t in skill_trees:
        x = deque(skill)
        for s in s_t:
            if s in x and s != x.popleft():
                break
        else:
            answer += 1
    return answer
