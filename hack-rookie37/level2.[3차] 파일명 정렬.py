import re


def solution(files):
    answer = []

    for i, f in enumerate(files):
        HEAD = re.match(r"[^0-9]+", f).group()
        N_T = re.search(r"[0-9]+", f)
        NUMBER = N_T.group()
        TAIL = f[N_T.end() :]
        answer.append((i, HEAD, NUMBER, TAIL))

    answer.sort(key=lambda x: (x[1].lower(), int(x[2]), x[0]))

    return ["".join(x[1:]) for x in answer]
