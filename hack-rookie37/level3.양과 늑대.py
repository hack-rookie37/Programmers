def solution(info, edges):
    tree = [list() for _ in range(len(info))]
    for p, c in edges:
        tree[p].append(c)

    def search(s, w, c, path):
        if info[c]:
            w += 1
        else:
            s += 1

        if s <= w:
            return 0

        maxSheep = s

        for p in path:
            for n in tree[p]:
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep, search(s, w, n, path))
                    path.pop()
        return maxSheep

    answer = search(0, 0, 0, [0])

    return answer
