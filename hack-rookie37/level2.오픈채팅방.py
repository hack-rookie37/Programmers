def solution(record):
    answer = []

    d = dict()

    for r in record:
        act, *uid = r.split()

        if act != "Leave":
            d[uid[0]] = uid[1]

    for r in record:
        act, *uid = r.split()

        if act == "Change":
            continue

        msg = d[uid[0]] + "님이 "

        if act == "Enter":
            msg += "들어왔습니다."
        elif act == "Leave":
            msg += "나갔습니다."

        answer.append(msg)

    return answer
