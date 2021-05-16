from sys import stdin
from collections import deque

n, k = list(map(int, stdin.readline().split()))


def bfs():
    queue = deque()
    queue.append((n, 0))
    while queue:
        cur = queue.popleft()
        if 2 * cur[0] == k: return cur[1]
        elif cur[0]+1 == k or cur[0]-1 == k: return cur[1]+1
        if cur[0] < k and 2*cur[0] < 100001:
            queue.appendleft((2*cur[0], cur[1]))
        if cur[0] < 100000:
            queue.append((cur[0]+1, cur[1]+1))
        if cur[0] > 0:
            queue.append((cur[0]-1, cur[1]+1))


print(bfs())
