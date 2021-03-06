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


def dfs(now_i, now_j, level, now_sum):
    if level == K:
        global res
        res = max(res, now_sum)
        return
    
    for near_i, near_j in near_idx:
        temp_i, temp_j = now_i+near_i, now_j+near_j
        if temp_i<N and temp_j<M:
            near_check[temp_i][temp_j] += -1

    for j in range(now_j+1, M):
        if near_check[now_i][j] == 0:
            dfs(now_i, j, level+1, now_sum+grid[now_i][j])

    for i in range(now_i+1, N):
        for j in range(M):
            if near_check[i][j] == 0:
                dfs(i, j, level+1, now_sum+grid[i][j])
    
    for near_i, near_j in near_idx:
        temp_i, temp_j = now_i+near_i, now_j+near_j
        if temp_i<N and temp_j<M:
            near_check[temp_i][temp_j] += 1

if __name__ == "__main__":
    N, M, K = map(int, input().rstrip().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().rstrip().split())))

    near_idx = [[0, 1], [1, 0]]
    near_check = [[0]*M for _ in range(N)]
    res = -40001
    for start_i in range(N):
        for start_j in range(M):
            dfs(start_i, start_j, 1, grid[start_i][start_j])
    print(res)