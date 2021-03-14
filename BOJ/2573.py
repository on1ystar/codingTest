from sys import stdin
from collections import deque
from copy import deepcopy

def find_ice(i, j, next_north):
    global visited, now_finded
    q = deque([(i, j)])
    ice_idx = []
    while q:
        i, j = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = True
        now_finded += 1
        cnt = 0
        for d_i, d_j in direct:
            next_i, next_j = i + d_i, j + d_j
            if 0 <= next_i < N and 0 <= next_j < M:
                if now_north[next_i][next_j] != 0:
                    q.append((next_i, next_j))
                else:
                    cnt += 1
        if now_north[i][j] > cnt:
            next_north[i][j] = now_north[i][j] - cnt
            ice_idx.append((i, j))
        else:
            next_north[i][j] = 0
    return next_north, ice_idx

if __name__ == "__main__":
    N, M = map(int, input().split())
    now_north = []
    now_ice_idx = []
    for i in range(N):
        now_north.append(list(map(int, stdin.readline().rstrip().split())))
        now_ice_idx += [[i,j] for j in range(M) if now_north[i][j] != 0]
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    year = 0
    while True:
        if len(now_ice_idx) == 0: 
            print(0)
            break
        visited = [[False] * M for _ in range(N)]
        now_finded = 0
        now_north, next_ice_idx = find_ice(now_ice_idx[0][0], now_ice_idx[0][1], deepcopy(now_north))
        if now_finded != len(now_ice_idx):
            print(year)
            break
        year += 1
        now_ice_idx = next_ice_idx
