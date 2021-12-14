n = int(input())
li = list(map(int, input().rstrip().split()))
li.sort()
group = 0
while n != 0:
    x = li[-1]
    for _ in range(x):
        li.pop()
        n -= 1
    if n < 0: break
    group += 1
print(group)