N, M = map(int, input().rstrip().split())
li = []
min_n = 0
for i in range(N):
    li.append(list(map(int, input().rstrip().split())))
for l in li:
    n = min(l)
    if n > min_n:
        min_n = n
print(min_n)
