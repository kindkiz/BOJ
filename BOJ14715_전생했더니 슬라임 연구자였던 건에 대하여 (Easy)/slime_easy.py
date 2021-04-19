from sys import stdin
n = int(stdin.readline())
cnt, p = 0, 2
while n > 1:
    if n % p == 0:
        cnt += 1
        n /= p
    else:
        p += 1
res = 0
k = 1
while k < cnt:
    k *= 2
    res += 1
print(res)
