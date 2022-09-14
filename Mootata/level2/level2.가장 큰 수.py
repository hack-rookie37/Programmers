def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x * 3, reverse=True)
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))

# lambda에서 x * 3을 하는 이유는 30과 3이 있을 떄 3이 30보다 앞에 와야하기 때문에
#  303030과 333을 비교하여 333이 더 앞에 위치하도록 함

# 문자열의 크기비교는 아스키코드 값을 통해 하기 때문에 숫자의 크기가 아닌
# 각각의 자리에 오는 값의 크기를 통해 정렬함.
# 303030과 333의 경우에 맨 앞자리의 3은 동일하고, 두번째 자리의 수가 각각 0과 3이기 때문에
# 두번째 자리의 크기가 더 큰 333이 303030보다 앞쪽에 위치함.