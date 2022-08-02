from collections import defaultdict

def solution(record):
    answer = []
    dic = defaultdict(str)
    status = []
    
    for i in record:
        commands = i.split()
        if commands[0] == "Enter":
            dic[commands[1]] = commands[2]
            status.append((commands[0], commands[1]))
        elif commands[0] == "Change":
            dic[commands[1]] = commands[2]
        else:
            status.append((commands[0], commands[1]))
        
    
    for i in status:
        if i[0] == "Enter":
            answer.append(dic[i[1]] + "님이 들어왔습니다.")
        else:
            answer.append(dic[i[1]] + "님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))