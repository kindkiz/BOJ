from sys import stdin
import heapq
p_heap = []
n_heap = []

n = int(stdin.readline())

for i in range(n):
    num = int(stdin.readline())
    if num == 0:
        if not (p_heap or n_heap):
            print(0)
            continue
        else:
            pn = float('inf')
            nn = float('inf')
            if p_heap:
                pn = p_heap[0]
            if n_heap:
                nn = n_heap[0]
            if pn < nn:
                print(heapq.heappop(p_heap))
            else:
                print(heapq.heappop(n_heap) * (-1))
    else:
        if num > 0:
            heapq.heappush(p_heap, num)
        else:
            heapq.heappush(n_heap, num * (-1))
