from sys import stdin
from collections import deque
nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]

n = int(stdin.readline())
board = [stdin.readline() for i in range(n)]
check = [[False] * n for i in range(n)]
apt = []


def bfs(start):
    queue = deque()
    queue.append(start)
    check[start[0]][start[1]] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx < 0 or dy < 0: continue
            if dx >= n or dy >= n: continue
            if check[dx][dy]: continue
            if board[dx][dy] == '0': continue
            check[dx][dy] = True
            cnt += 1
            queue.append((dx, dy))
    return cnt


for i in range(n):
    for j in range(n):
        if check[i][j] or board[i][j] == '0':
            continue
        apt.append(bfs((i, j)))
apt.sort()
print(len(apt))
for i in apt:
    print(i)
