from sys import stdin

n = int(stdin.readline())
m = 1
cnt = 0


def findm(num):
    tmp = 1
    while tmp < num:
        tmp = tmp << 1
    tmp = tmp >> 1
    return tmp


while n > 1:
    m = findm(n)
    n -= m
    cnt += 1
print(1) if cnt % 2 == 1 else print(0)
