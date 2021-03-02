# N과 M (2)

from itertools import combinations

N, M = map(int, input().rstrip().split())
for p in list(map(" ".join, combinations(map(str, range(1, N+1)),M))):
    print(p)
