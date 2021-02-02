from collections import deque

def dfs(v, cnt):
    if cnt > K:
        return
    cnt += 1
    for next in street_map[v]:
        if next in city.keys():
            if city[next] > cnt:
                city[next] = cnt
        else:
            city[next] = cnt
        dfs(next, cnt)


N, M, K, X = map(int, input().rstrip().split())
street_map = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    street_map[A].append(B)

city = {}
city_k = []
dfs(X, 0)
for c in city:
    if city[c] == K:
        city_k.append(c)
if len(city_k) == 0:
    print(-1)
else:
    for c in sorted(city_k):
        print(c)