def solution(progresses, speeds):
    answer = []
    job = []

    for p, s in zip(progresses, speeds):
        q, r = divmod(100 - p, s)

        if r > 0:
            job.append(q + 1)
        else:
            job.append(q)

    days = job[0]
    t = 0
    for j in job:
        if j > days:
            answer.append(t)
            days = j
            t = 1
        else:
            t += 1

    answer.append(t)

    return answer
