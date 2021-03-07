# 연산자 끼워넣기


def dfs(res, sq_idx, plus, sub, multi, div):
    if sq_idx == N-1:
        global max_res, min_res
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return

    if plus: dfs(res+sequence[sq_idx+1], sq_idx+1, plus-1, sub, multi, div)
    if sub: dfs(res-sequence[sq_idx+1], sq_idx+1, plus, sub-1, multi, div)
    if multi: dfs(res*sequence[sq_idx+1], sq_idx+1, plus, sub, multi-1, div)
    if div: 
        if res < 0: dfs(-(abs(res)//sequence[sq_idx+1]), sq_idx+1, plus, sub, multi, div-1)
        else: dfs(res//sequence[sq_idx+1], sq_idx+1, plus, sub, multi, div-1)
            
if __name__ == "__main__":
    N = int(input())
    sequence = list(map(int, input().split()))
    oper_list = list(map(int, input().split()))
    max_res, min_res = -10**9, 10**9
    dfs(sequence[0], 0, oper_list[0], oper_list[1], oper_list[2], oper_list[3])
    print(max_res, min_res, sep="\n")