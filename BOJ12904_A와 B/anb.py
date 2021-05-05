from sys import stdin
from collections import deque
S = stdin.readline().strip()
T = stdin.readline().strip()
s, t = deque([i for i in S]), deque([i for i in T])


while s != t and len(t) > 0:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        temp = []
        while t:
            temp.append(t.pop())
        t = deque(temp)
if s == t:
    print(1)
else:
    print(0)
