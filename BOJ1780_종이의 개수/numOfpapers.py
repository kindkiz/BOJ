from sys import stdin
n = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for i in range(n)]
ans = [0] * 3


def check(x1, y1, x2, y2):
    tmp = paper[x1][y1]
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if tmp != paper[i][j]:
                return False
    return True


def recursion(x1, y1, x2, y2, n):
    global ans
    if check(x1, y1, x2, y2):
        ans[paper[x1][y1]+1] += 1
        return
    inc = int(n/3)
    for i in range(3):
        for j in range(3):
            recursion(x1 + i*inc, y1 + j*inc, x2 - (2-i)*inc, y2 - (2-j)*inc, inc)


recursion(0, 0, n-1, n-1, n)
for i in ans:
    print(i)
