from sys import stdin
import heapq

n = int(stdin.readline())
ppq = []
npq = []
sum = 0


def cal(pq):
    global sum
    while len(pq) > 1:
        a = heapq.heappop(pq)[1]
        b = heapq.heappop(pq)[1]
        if a <= 0 < b or a == 1 or b == 1:
            sum += a
            sum += b
        else:
            sum += a * b
    if pq:
        sum += pq.pop()[1]


for i in range(n):
    tmp = int(stdin.readline())
    if tmp > 0:
        heapq.heappush(ppq, (-tmp, tmp))
    else:
        heapq.heappush(npq, (tmp, tmp))

cal(npq)
cal(ppq)
print(sum)
