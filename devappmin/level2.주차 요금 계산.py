from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []

    car_dicts = defaultdict(list)
    car_time_dicts = defaultdict(float)

    for record in records:
        time, car_num, action = record.split()
        hour, minute = map(int, time.split(':'))
        time = hour * 60 + minute
        if action == 'IN':
            car_dicts[car_num].append(time)
        else:
            car_time_dicts[car_num] += time - car_dicts[car_num].pop()


    for key, car_list in car_dicts.items():
        if car_list:
            car_time_dicts[key] += 1439 - car_list.pop()

    for key, value in sorted(car_time_dicts.items()):
        answer.append(fees[1] + max(0, ceil((value - fees[0]) / fees[2]) * fees[3]))

    return answer

# Test Case
test_cases = [
                [[180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]], 
                [[120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]],
                [[1, 461, 1, 10], ["00:00 1234 IN"]]
            ]
test_cases_answer = [[14600, 34400, 5000], [0, 591], [14841]]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")