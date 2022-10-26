from collections import defaultdict
from math import ceil


def solution(fees, records):
    min_t, min_f, per_t, per_f = fees

    table = defaultdict(int)
    time_in = defaultdict(int)

    for row in records:
        time, number, action = row.split()
        hh, mm = map(int, time.split(":"))

        if action == "IN":
            time_in[number] = hh * 60 + mm

        else:
            table[number] += (hh * 60 + mm) - time_in[number]
            del time_in[number]

    if time_in:
        for number in time_in:
            table[number] += (23 * 60 + 59) - time_in[number]

    answer = []
    for number in sorted(table):
        if table[number] <= min_t:
            answer.append(min_f)
        else:
            fee = min_f
            fee += (ceil((table[number] - min_t) / per_t)) * per_f
            answer.append(fee)

    return answer
