from collections import deque


direction = {
    'E' : (0, 1),
    'N' : (-1, 0),
    'W' : (0, -1),
    'S' : (1, 0)
}

def get_adjacent(pos):
    adj_pos_list = []
    for d in direction.values():
        i, j = pos[0] + d[0], pos[1] + d[1]
        if 0 <= i < N and 0 <= j < M :
            if ice_frame[i][j] == '0':
                adj_pos_list.append(i*N+i+j)
    return adj_pos_list


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M = map(int, input().rstrip().split())
ice_frame = []
graph = [[] for _ in range(N*M)]
for _ in range(N):
    ice_frame.append([x for x in input()])

for i in range(N):
    for j in range(M):
        if ice_frame[i][j] == '0':
            graph[i*N+i+j] = get_adjacent((i,j))

visited = [False] * (N*M)
icecream = 0
for i in range(N):
    for j in range(M):
        if ice_frame[i][j] == '0' and visited[i*N+i+j] == False:
            icecream += 1
            bfs(graph, i*N+i+j, visited)

print(icecream)