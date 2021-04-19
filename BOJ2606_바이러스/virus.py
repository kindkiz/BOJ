from sys import stdin
from collections import deque
n = int(stdin.readline())
com = int(stdin.readline())
check = [False] * (n+1)
adj = {i: [] for i in range(n+1)}
for i in range(com):
    node1, node2 = list(map(int, stdin.readline().split()))
    adj[node1].append(node2)
    adj[node2].append(node1)


def bfs():
    queue = deque()
    queue.append(1)
    check[1] = True
    while queue:
        current = queue.popleft()
        for next_node in adj[current]:
            if check[next_node]: continue
            check[next_node] = True
            queue.append(next_node)


bfs()
count = -1
for v in check:
    if v:
        count += 1

print(count)
