from sys import stdin
import heapq
n, t, p = list(map(int, stdin.readline().split()))
minecraft = list(map(int, stdin.readline().split()))
MAX = 0
queue = []
sum = 0
for i in range(n):
    count = 0
    w = i * p
    if w > t:
        break
    heapq.heappush(queue, (-minecraft[i], minecraft[i]))
    sum += minecraft[i]
    while queue and sum + w > t:
        sum -= heapq.heappop(queue)[1]
    MAX = max(MAX, len(queue))
print(MAX)
