def solution(n):

    bn = list(bin(n))
    one = bn.count("1")

    x = n + 1

    while x <= 1000000:
        bx = list(bin(x))

        if bx.count("1") == one:
            break

        x += 1

    return x
