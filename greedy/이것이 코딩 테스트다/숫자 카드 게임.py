N, M = map(int, input().split())
matrix = []
mins = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
for row in matrix:
    mins.append(min(row))
print(max(mins))