def solution(phone_book):
    phone_book.sort()
    hash = set()
    for num in phone_book:
        t = ""
        for n in num:
            t += n
            if t in hash:
                return False
        hash.add(num)
    return True
