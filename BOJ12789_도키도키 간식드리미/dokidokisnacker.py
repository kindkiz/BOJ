from sys import stdin
from collections import deque
n = int(stdin.readline())
origin = deque(list(map(int, stdin.readline().split())))
stack = deque()
cnt = 1
while origin or stack:
    tmp1, tmp2 = n+1, n+1
    if origin: tmp1 = origin[0]
    if stack: tmp2 = stack[-1]
    if cnt == tmp1:
        origin.popleft()
        cnt += 1
    elif cnt == tmp2:
        if min(stack) != cnt:
            print("Sad")
            exit(0)
        stack.pop()
        cnt += 1
    elif cnt < tmp1 and origin:
        stack.append(origin.popleft())
    else:
        print("Sad")
        exit(0)
else:
    print("Nice")
