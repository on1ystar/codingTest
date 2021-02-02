def dfs(maze, i, j, cnt):
    if i+1 == N and j+1 == M:
        find_cnt.append(cnt + 1)
        return
    if 0 <= i < N and 0 <= j < M and maze[i][j] == 1:
        new_maze = maze.copy()
        new_maze[i][j] = 0
        cnt += 1
        dfs(new_maze, i+1, j, cnt)
        dfs(new_maze, i, j+1, cnt)
        dfs(new_maze, i-1, j, cnt)
        dfs(new_maze, i, j-1, cnt)
    else:
        return

N, M = map(int, input().rstrip().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))
find_cnt = []
dfs(maze, 0, 0, cnt = 0)
print(find_cnt)
print(min(find_cnt))