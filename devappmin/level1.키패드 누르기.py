from collections import defaultdict

def solution(numbers, hand):
    answer = ''

    graph = defaultdict(tuple)
    for idx in range(1, 10):
        graph[idx] = ((idx - 1) // 3, ( idx - 1 ) % 3)
    graph[0] = (3, 1)

    left, right = (3, 0), (3, 2)

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            left = graph[number]
            continue
        
        if number == 3 or number == 6 or number == 9:
            answer += "R"
            right = graph[number]
            continue

        left_dist = abs(left[0] - graph[number][0]) + abs(left[1] - graph[number][1])
        right_dist = abs(right[0] - graph[number][0]) + abs(right[1] - graph[number][1])

        if left_dist < right_dist:
            answer += "L"
            left = graph[number]
            continue

        if left_dist > right_dist:
            answer += "R"
            right = graph[number]
            continue
        
        if hand == "left":
            answer += "L"
            left = graph[number]
            continue

        if hand == "right":
            answer += "R"
            right = graph[number]

    return answer

# Test Case
test_cases = [  [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"], 
                [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"],
                [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]]
for test_case in test_cases:
    print(solution(*test_case))