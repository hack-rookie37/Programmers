from collections import defaultdict

def solution(genres, plays):
    
    dicts = defaultdict(list)
    total = defaultdict(int)
    answer = []
    for genre, plays, idx in zip(genres, plays, range(len(plays))):
        dicts[genre].append((plays, idx))
        total[genre] += plays
        
    for genre, _ in sorted(total.items(), key=lambda a: -a[1]):
        if len(dicts[genre]) <= 1:
            answer.append(dicts[genre][0][1])
            continue
        answer.extend(x for _, x in sorted(dicts[genre], key=lambda a: (-a[0], a[1]))[:2])
        
    return answer

# Test Case
test_cases = [
                [["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]], 
            ]
test_cases_answer = [[4, 1, 3, 0]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")