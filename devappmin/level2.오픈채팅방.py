from collections import defaultdict

def solution(record):
    answer = []
    actions = []
    uid_dicts = defaultdict(str)
    
    for cmd in record:
        cmd = cmd.split()
        
        actions.append((cmd[0], cmd[1]))
        
        if cmd[0] == 'Enter' or cmd[0] == 'Change':
            uid_dicts[cmd[1]] = cmd[2]
            
    for action, uid in actions:
        if action == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(uid_dicts[uid]))
        elif action == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(uid_dicts[uid]))
    
    return answer

# Test Case
test_cases = [[["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]]]
for test_case in test_cases:
    print(solution(*test_case))