def solution(s):
    return int(s
    .replace('zero', '0')
    .replace('one', '1')
    .replace('two', '2')
    .replace('three', '3')
    .replace('four', '4')
    .replace('five', '5')
    .replace('six', '6')
    .replace('seven', '7')
    .replace('eight', '8')
    .replace('nine', '9')
    )

# Test Case
test_cases =    [
                ["one4seveneight"], 
                ["23four5six7"],
                ["2three45sixseven"],
                ["123"]
                ]
for test_case in test_cases:
    print(solution(*test_case))