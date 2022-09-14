def solution(s):
    count = zero = 0

    while s != "1":
        count += 1
        x = "".join(filter(lambda x: x == "1", s))
        Ls, Lx = len(s), len(x)
        zero += Ls - Lx
        s = str(bin(Lx))[2:]

    return [count, zero]
