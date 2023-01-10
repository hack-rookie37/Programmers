from collections import defaultdict, deque


def solution(n, wires):
    answer = n - 1
    half = n // 2
    ideal = (half, half) if n % 2 == 0 else (half, half + 1)
    tree = defaultdict(list)

    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)

    for v1, v2 in wires:
        visited = set([1])
        q = deque([1])
        while q:
            node = q.pop()
            for nxt in tree[node]:
                if nxt in visited:
                    continue
                if (v1 == node and v2 == nxt) or (v1 == nxt and v2 == node):
                    continue
                q.append(nxt)
                visited.add(nxt)

        len_visited = len(visited)
        if len_visited == ideal[0] or len_visited == ideal[1]:
            return abs(ideal[0] - ideal[1])
        answer = min(answer, abs(n - 2 * len_visited))

    return answer
