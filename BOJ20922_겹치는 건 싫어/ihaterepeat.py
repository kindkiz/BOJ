from sys import stdin
n, k = list(map(int, stdin.readline().split()))

arr = list(map(int, stdin.readline().split()))
check = [0] * 100001
l = 0
r = 0
MAX = 0
flag = False
for i in arr:
    check[i] += 1
    while check[i] > k:
        check[arr[l]] -= 1
        l += 1
    MAX = max(MAX, r-l+1)
    r += 1

print(MAX)