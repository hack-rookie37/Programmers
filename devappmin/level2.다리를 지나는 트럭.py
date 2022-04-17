
def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    answer = 0

    while bridge:
        bridge.pop(0)
        answer += 1

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                while bridge[0] == 0:
                    bridge.pop(0)
                    bridge.append(0)
                    answer += 1

                bridge.append(0)

    return answer

# Test Case
test_cases = [[2, 10, [7, 4, 5, 6]], [100, 100, [10]], [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]]
for test_case in test_cases:
    print(solution(*test_case))