from collections import deque
import sys

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]


def bfs(w, h, i, j):
    queue = deque([(i, j)])
    island[i][j] = 0
    while queue:
        i, j = queue.popleft()
        for d in range(8):
            next_i = i + dx[d]
            next_j = j + dy[d]
            if 0 <= next_i < h and 0 <= next_j < w:
                if island[next_i][next_j] == 1:
                    island[next_i][next_j] = 0
                    queue.append((next_i, next_j))

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    island = []
    island_cnt = 0
    for _ in range(h):
        island.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(w, h, i, j)
                island_cnt += 1
    print(island_cnt)
