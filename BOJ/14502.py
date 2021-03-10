# 연구소


from collections import deque
import copy

def start(copied_map, new_savend_cnt):
    visited = [False] * map_size
    q = deque(virus_pos)
    while q:
        c = q.popleft()
        if visited[c]: continue
        visited[c] = True
        for i, j in direct:
            next_row = (c // M) + i
            next_col = (c % M) + j
            if 0 <= next_row < N and 0 <= next_col < M and copied_map[next_row][next_col] == 0:
                copied_map[next_row][next_col] = 2
                q.append(next_row * M + next_col)
                new_savend_cnt -= 1
    return copied_map, new_savend_cnt

def set_defense(block):
    row, col = (block // M), (block % M)
    if ins_map[row][col] == 0:
        ins_map[row][col] = 1
        return True
    else:
        return False
            

def re_defense(block):
    row, col = (block // M), (block % M)
    ins_map[row][col] = 0
    return 1

if __name__ == "__main__":
    N, M = map(int, input().split())
    ins_map = []
    virus_pos = []
    saved_cnt = -3
    for i in range(N):
        ins_map.append(list(map(int, input().split())))
        for j in range(M):
            if ins_map[i][j] == 2: virus_pos.append(i * M + j)
            elif ins_map[i][j] == 0: saved_cnt += 1
    map_size = N*M
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 위, 오, 아, 왼
    max_res = 0
    for i in range(map_size):
        if not set_defense(i): continue
        for j in range(i+1, map_size):
            if not set_defense(j): continue
            for k in range(j+1, map_size):
                if not set_defense(k): continue
                infected_map, res = start(copy.deepcopy(ins_map), saved_cnt)
                max_res = max(max_res, res)
                re_defense(k)
            re_defense(j)
        re_defense(i)
    print(max_res)