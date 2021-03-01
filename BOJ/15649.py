from itertools import permutations

N, M = map(int, input().rstrip().split())
for p in list(map(" ".join, permutations(map(str, range(1, N+1)),M))):
    print(p)
