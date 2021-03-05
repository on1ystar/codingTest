#  NM과 K (1)

# 조합으로 모든 조합 탐색
# python3은 시간 초과, pypy3은 3312ms
# from itertools import combinations, product


# N, M, K = map(int, input().rstrip().split())
# grid = []
# near_idx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# res = []
# for _ in range(N):
#     grid.append(list(map(int, input().rstrip().split())))

# all_combi = combinations(product([x for x in range(N)], [x for x in range(M)]), K)
# for combi in all_combi:
#     combi_sum = 0
#     near = False
#     for i, j in combi:
#         for near_i, near_j in near_idx:
#             if (i+near_i, j+near_j) in combi: 
#                 near = True
#                 break
#         if near: 
#             break
#         else:
#             combi_sum += grid[i][j]
#     if not near: 
#         res.append(combi_sum)
# print(max(res))






def dfs(now_i, now_j):
    global res
    if len(selected_nums) == K:
        res = max(res, sum(selected_nums))
        return
    
    for near_i, near_j in near_idx:
        temp_i, temp_j = now_i+near_i, now_j+near_j
        if 0<=temp_i<N and 0<=temp_j<M:
            visited[temp_i][temp_j] += -1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                selected_nums.append(grid[i][j])
                visited[i][j] = 1
                dfs(i, j)
                selected_nums.pop()
                visited[i][j] = 0

if __name__ == "__main__":
    N, M, K = map(int, input().rstrip().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().rstrip().split())))

    near_idx = [[0, 1], [1, 0]]
    visited = [[0]*M for _ in range(N)]
    res = 0
    selected_nums = []
    for start_i in range(N):
        for start_j in range(M):
            selected_nums.append(grid[start_i][start_j])
            visited[start_i][start_j] = 1
            dfs(start_i, start_j)
            selected_nums.pop()
    print(res)