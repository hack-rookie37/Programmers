def solution(arr):
    result = [0, 0]
    length = len(arr)

    def compress(a, b, l):
        bit = arr[a][b]
        for i in range(a, a + l):
            if (bit and not all(arr[i][b : b + l])) or (
                not bit and any(arr[i][b : b + l])
            ):
                l = l // 2
                compress(a, b, l)
                compress(a, b + l, l)
                compress(a + l, b, l)
                compress(a + l, b + l, l)
                return

        result[bit] += 1

    compress(0, 0, length)

    return result
