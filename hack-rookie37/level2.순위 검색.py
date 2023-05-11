from collections import defaultdict
from itertools import product


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


def solution(info, query):

    db = defaultdict(list)
    for i in info:
        s = i.split()
        key = "".join(map(lambda x: x[0], s[:-1]))
        score = int(s[-1])

        key = list(zip(key, "----"))
        for bit in product(range(2), repeat=4):
            code = ""
            for n, b in enumerate(bit):
                code += key[n][b]
            db[code].append(score)

    [db[key].sort() for key in db.keys()]

    answer = []
    for q in query:
        s = q.replace("and", " ").split()
        key = "".join(map(lambda x: x[0], s[:-1]))
        score = int(s[-1])

        answer.append(len(db[key]) - binary_search(score, db[key]))

    return answer
