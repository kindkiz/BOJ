from sys import stdin
n, m = list(map(int, stdin.readline().split()))

p = list(map(int, stdin.readline().split()))
x = list(map(int, stdin.readline().split()))
md = 0
dist = [0] * 1000001
for i in range(n):
    dist[p[i]] = max(p[i] + x[i], dist[p[i]])
    md = max(md, p[i] + x[i])

if md < m:
    print('-1')
    exit(0)

start = p[0] + x[0]
pre = p[0]
cnt = 0

while start < m:
    MAX = -1
    idx = 0
    for i in range(pre, start+1):
        if i > m:
            break
        if MAX < dist[i]:
            MAX = dist[i]
    if MAX == -1:
        print('-1')
        exit(0)
    pre = start+1
    start = MAX
    cnt += 1
print(cnt)
