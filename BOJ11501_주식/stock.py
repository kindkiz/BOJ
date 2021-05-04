from sys import stdin
tc = int(stdin.readline())

while tc > 0:
    tc -= 1
    n = int(stdin.readline())
    stock = list(map(int, stdin.readline().split()))
    max = stock[-1]
    money = 0
    for i in range(n-2, -1, -1):
        if stock[i] < max:
            money += max - stock[i]
        else:
            max = stock[i]
    print(money)
