from sys import stdin
from collections import deque

n, p = list(map(int, stdin.readline().split()))
stacks = list(deque() for i in range(n+1))
res = 0

for i in range(n):
    line, pt = list(map(int, stdin.readline().split()))
    while stacks[line] and stacks[line][-1] > pt:
            res += 1
            stacks[line].pop()
    if stacks[line] and stacks[line][-1] == pt:
        continue
    stacks[line].append(pt)
    res += 1

print(res)
