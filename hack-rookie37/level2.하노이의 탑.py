def solution(n):
    answer = []

    def hanoi(n, _from, _to, _via):
        if n == 1:
            answer.append([_from, _to])
            return

        hanoi(n - 1, _from, _via, _to)
        answer.append([_from, _to])
        hanoi(n - 1, _via, _to, _from)

    hanoi(n, 1, 3, 2)

    return answer

solution(3)