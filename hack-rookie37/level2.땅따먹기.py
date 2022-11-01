def solution(land):
    L = len(land)

    for i in range(1, L):
        for x in range(4):
            land[i][x] = max(land[i-1][m] + land[i][x] for m in range(4) if m != x)
        
        # same as
        # land[i][0] = max(land[i-1][1], land[i-1][2], land[i-1][3]) + land[i][0]
        # land[i][1] = max(land[i-1][0], land[i-1][2], land[i-1][3]) + land[i][1]
        # land[i][2] = max(land[i-1][0], land[i-1][1], land[i-1][3]) + land[i][2]
        # land[i][3] = max(land[i-1][0], land[i-1][1], land[i-1][2]) + land[i][3]
        # this is faster

    return max(land[-1])
