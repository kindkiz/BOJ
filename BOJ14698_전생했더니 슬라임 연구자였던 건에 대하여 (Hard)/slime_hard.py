from sys import stdin
import heapq

tc = int(stdin.readline())
for i in range(tc):
    queue = []
    total_energy = 1
    n = int(stdin.readline())
    slime = list(map(int, stdin.readline().split()))
    for energy in slime:
        heapq.heappush(queue, energy)
    while len(queue) > 1:
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)
        total_energy *= (a*b) % 1000000007
        heapq.heappush(queue, a*b)
    print(total_energy % 1000000007)
