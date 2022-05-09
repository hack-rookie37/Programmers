from itertools import permutations

def calculate(ex, n, formula):
    if n == 2: # 수식 3개에 대해서 모두 연산이 끝났을 때 종료
        return str(eval(formula))
    if ex[n] == '*': # 우선순위의 반대 순서로 식을 쪼개서 재귀
        result = eval('*'.join([calculate(ex, n + 1, f) for f in formula.split('*')]))
    if ex[n] == '+':
        result = eval('+'.join([calculate(ex, n + 1, f) for f in formula.split('+')]))
    if ex[n] == '-':
        result = eval('-'.join([calculate(ex, n + 1, f) for f in formula.split('-')]))
    return str(result)

def solution(formula):
    answer = 0
    ex = list(permutations(['*', '+', '-'], 3)) # 가능한 모든 우선순위 생성
    
    for i in ex: # 각 우선순위 별 최대값 구함
        result = int(calculate(i, 0, formula))
        answer = max(answer, abs(result))
    
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))

# 예를 들어 - > * > + 순서라면 + 연산을 진행하기 위해서는 * 연산의 결과가 필요하고, + 연산을 하기 위해서는 - 연산의 결과가 필요하기 때문에
# 가장먼저 식을 +를 기준으로 쪼개고, 그 식을 다시한번 *를 기준으로 쪼갠 뒤 eval을 통해 - 연산을 진행하고 그 결과 값을 가지고 나머지 연산도
# 진행하는 방식