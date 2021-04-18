from sys import stdin
from collections import deque


adj = {i: [] for i in range(1001)}
n, m, v = list(map(int, stdin.readline().split()))
check = [False] * (n+1)
for i in range(m):
    node1, node2 = list(map(int, stdin.readline().split()))
    adj[node1].append(node2)
    adj[node2].append(node1)

for i in range(1, n+1):
    adj[i].sort()


def dfs(start):
    check[start] = True
    print(start, end=' ')
    for next_node in adj[start]:
        if check[next_node]: continue
        check[next_node] = True
        dfs(next_node)


def bfs(start):
    check[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for next_node in adj[current]:
            if check[next_node]: continue
            check[next_node] = True
            queue.append(next_node)


dfs(v)
print()
check = [False] * (n+1)
bfs(v)
