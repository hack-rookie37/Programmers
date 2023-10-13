def solution(cap, n, deliveries, pickups):
    ds = deliveries
    ps = pickups

    answer = 0

    d, p = [], []
    for i in range(n):
        if ds[i]:
            d.append(i)
        if ps[i]:
            p.append(i)

    di, pi = len(d) - 1, len(p) - 1
    while di >= 0 or pi >= 0:
        longest = [0, 0]
        dcap = cap
        while dcap:
            if di < 0:
                break
            if ds[d[di]] > dcap:
                ds[d[di]] -= dcap
                dcap = 0
                if longest[0] == 0:
                    longest[0] = d[di] + 1
            else:
                dcap -= ds[d[di]]
                ds[d[di]] = 0
                if longest[0] == 0:
                    longest[0] = d[di] + 1
                di -= 1

        pcap = cap
        while pcap:
            if pi < 0:
                break
            if ps[p[pi]] > pcap:
                ps[p[pi]] -= pcap
                pcap = 0
                if longest[1] == 0:
                    longest[1] = p[pi] + 1
            else:
                pcap -= ps[p[pi]]
                ps[p[pi]] = 0
                if longest[1] == 0:
                    longest[1] = p[pi] + 1
                pi -= 1

        answer += max(longest) * 2

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
