truck_weights = [10]
weight = 100
bridge_length = 100
trucks = [0] * bridge_length
answer = 0

while trucks:
    trucks.pop(0)
    answer += 1
    if truck_weights:
        if truck_weights[0] + sum(trucks) <= weight:
            trucks.append(truck_weights.pop(0))
        else:
            trucks.append(0)

print(answer)
