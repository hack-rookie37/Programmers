from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append((list(begin), 0))
    visited = []
    while q:
        w, count = q.popleft()
        if ''.join(w) == target:
            return count
            
        for word in words:
            for i in range(len(word)): # words에 있는 각 단어의 알파벳으로 한자리씩 변경 begin = hit 이면 word가 lot 일때 lit, hot 두 단어가 만들어짐
                temp = w[:]
                if temp[i] != word[i]:
                    temp[i] = word[i]
                    if (temp, count + 1) not in visited and ''.join(temp) in words: # 만들어진 적이 없고, words에 있는 단어로만 변경 가능
                        q.append((temp, count + 1))
                        visited.append((temp, count + 1))
    return 0

def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))