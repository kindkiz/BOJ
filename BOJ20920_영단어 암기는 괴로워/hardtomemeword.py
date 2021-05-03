from sys import stdin
n, m = list(map(int, stdin.readline().split()))
dict = {}


for i in range(n):
    word = stdin.readline().strip()
    if len(word) < m:
        continue
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

ndict = {}
for name, value in dict.items():
    if value in ndict:
        ndict[value].append(name)
    else:
        ndict[value] = [name]

for name, value in ndict.items():
    value.sort()
    value.sort(key=len, reverse=True)

for i in sorted(ndict.items(), reverse=True):
    for j in i[1]:
        print(j)
