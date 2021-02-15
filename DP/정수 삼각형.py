n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().rstrip().split())))
for layer in range(1,n):
    l = len(tri[layer])
    for i in range(l):
        temp = []
        if (0 <= i-1):
            temp.append(tri[layer-100][i-1])
        if (i < l-1):
            temp.append(tri[layer-1][i])
        tri[layer][i] += max(temp)
print(max(tri[n-1]))
