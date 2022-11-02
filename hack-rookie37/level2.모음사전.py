from itertools import product as pi


def solution(word):

    dic = ("A", "E", "I", "O", "U")

    return (
        sorted(["".join(p) for i in range(1, 6) for p in pi(dic, repeat=i)]).index(word)
        + 1
    )
