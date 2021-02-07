from sys import stdin
from collections import deque


N, M, K, X = map(int, input().rstrip().split())
street_map = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, stdin.readline().rstrip().split())
    street_map[A].append(B)
found_cities = [-1] * (N + 1)
found_cities[X] = 0
queue = deque([X])
while queue:
    city = queue.popleft()
    for next_city in street_map[city]:
        if found_cities[next_city] == -1:
            found_cities[next_city] = found_cities[city] + 1
            queue.append(next_city)

for city in range(len(found_cities)):
    if found_cities[city] == K:
        print(city)
if K not in found_cities: print(-1)