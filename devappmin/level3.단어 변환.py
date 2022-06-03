from collections import deque, defaultdict
from itertools import combinations

def check(word1, word2):
    diff = 0
    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            if diff: return False
            diff += 1
            
    return True if diff < 2 else False

def solution(begin, target, words):
    words.append(begin)
    visited = defaultdict(int)
    visited[begin] = 0
    
    dicts = defaultdict(list)
    
    for word1, word2 in combinations(words, 2):
        if check(word1, word2):
            dicts[word1].append(word2)
            dicts[word2].append(word1)
            
    q = deque([begin])
    
    while q:
        word = q.popleft()
        for sub_word in dicts[word]:
            if visited[sub_word]:
                continue
            
            q.append(sub_word)
            visited[sub_word] = visited[word] + 1
    
    return visited[target]

# Test Case
test_cases = [
                ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
                ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]
            ]
test_cases_answer = [4, 0]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")