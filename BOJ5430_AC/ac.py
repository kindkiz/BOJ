from sys import stdin
from collections import deque
t = int(stdin.readline())


for i in range(t):
    p = stdin.readline().strip()
    n = int(stdin.readline())
    cnt = 0
    queue = deque(stdin.readline().strip('[').strip().strip(']').split(','))
    if queue[0] == '':
        queue.popleft()
    flag = False
    for cmd in p:
        if cmd == 'D':
            if not queue:
                print('error')
                flag = True
                break
            else:
                if cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
        else:
            cnt += 1
    if flag:
        continue
    if cnt % 2 == 1:
        queue.reverse()
    print('[', end='')
    for idx, i in enumerate(queue):
        print(i, end='')
        if idx != len(queue) - 1:
            print(',', end='')
    print(']')
