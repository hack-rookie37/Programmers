sale = [40, 30, 20, 10]
answer = [0, 0]


def solution(users, emoticons):
    def dfs(slist, n):
        global answer
        if n >= len(emoticons) - 1:
            plus = 0
            t_price = 0
            for u_sale, u_price in users:
                price = 0
                for e_sale, e_price in slist:
                    if e_sale >= u_sale:
                        price += (e_price * (100 - e_sale)) // 100
                if price >= u_price:
                    plus += 1
                    price = 0
                t_price += price

            # update answer
            if answer[0] < plus:
                answer = [plus, t_price]
            elif answer[0] == plus:
                answer[1] = max(answer[1], t_price)
            return

        for x in sale:
            dfs(slist + [(x, emoticons[n + 1])], n + 1)

    for x in sale:
        dfs([(x, emoticons[0])], 0)

    return answer
