# 벽 부수고 이동하기 4

from sys import stdin, stdout

def dfs(pos):
    global visited
    if visited[pos]: 
        return 0
    visited[pos] = True
    row, col = (pos // M), (pos % M)
    res = 1
    for i, j in direct:
        next_row, next_col = row+i, col+j
        if 0 <= next_row < N and 0 <= next_col < M and input_map[next_row * M + next_col] == '0':
            res += dfs(next_row * M + next_col)
    return res

def crash(pos):
    res = 1
    row, col = (pos // M), (pos % M)
    for i, j in direct:
        next_row, next_col = row+i, col+j
        if 0 <= next_row < N and 0 <= next_col < M and input_map[next_row * M + next_col] == '0':
            res += movable[next_row * M + next_col]
    return res

if __name__ == "__main__":
    N, M = map(int, input().split())
    input_map = ""
    for _ in range(N):
        row = stdin.readline().rstrip()
        input_map += row
    map_size = N * M
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    result_map = [['0'] * M for _ in range(N)]

    movable = [0] * map_size  # 각 칸에서 이동할 수 있는 칸의 개수
    visited = [False] * map_size
    for pos in range(map_size):
        if input_map[pos] == '0':
            if visited[pos]:
                row, col = (pos // M), (pos % M)
                for i, j in direct:
                    next_row, next_col = row+i, col+j
                    if 0 <= next_row < N and 0 <= next_col < M and movable[next_row * M + next_col] != 0:
                         movable[pos] = movable[next_row * M + next_col]
                         break
            else: movable[pos] = dfs(pos) 

    for pos in range(map_size):
        if input_map[pos] == '1':
            result_map[pos // M][pos % M] = str(crash(pos) % 10)
    for row in result_map:
        stdout.write("".join(row) + '\n')