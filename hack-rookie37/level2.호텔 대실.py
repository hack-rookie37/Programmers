from datetime import datetime, timedelta
import heapq


def solution(book_time):

    book_time = sorted(
        [
            [
                datetime.strptime(s, "%H:%M"),
                datetime.strptime(e, "%H:%M") + timedelta(minutes=10),
            ]
            for s, e in book_time
        ]
    )

    pq = []
    answer = 1
    for s, e in book_time:
        if pq:
            if pq[0] <= s:
                heapq.heappop(pq)
            else:
                answer += 1
            heapq.heappush(pq, e)
        else:
            heapq.heappush(pq, e)

    return answer
