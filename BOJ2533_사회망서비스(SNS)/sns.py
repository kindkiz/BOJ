from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(1000001)

n = int(stdin.readline())
adj = [list() for i in range(n+1)]
v = [False] * (n+1)
v[1] = True
early = [False] * (n+1)
for i in range(n-1):
    node1, node2 = list(map(int, stdin.readline().split()))
    adj[node1].append(node2)
    adj[node2].append(node1)


def dfs(start):
    if len(adj[start]) == 1 and v[adj[start][0]]:
        return True
    for next_node in adj[start]:
        if v[next_node]:
            continue
        v[next_node] = True
        if dfs(next_node):
            early[start] = True
        v[next_node] = False
    if not early[start]:
        for child in adj[start]:
            if v[child]:
                continue
            if not early[child]:
                early[start] = True
                break


dfs(1)
ans = 0
for early_adaptor in early:
    if early_adaptor:
        ans += 1
print(ans)
