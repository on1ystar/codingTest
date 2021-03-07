# 부등호


def dfs(n, inequal_idx, used):
    if inequal_idx == K:
        global max_res, min_res
        max_res = max(max_res, int(used))
        min_res = min(min_res, int(used))
        return
    
    for next_n in map(str, range(10)):
        if next_n in used:
            continue
        if inequal_list[inequal_idx] == '>' and int(n) > int(next_n):
            dfs(next_n, inequal_idx+1, used + next_n)
        elif inequal_list[inequal_idx] == '<' and int(n) < int(next_n):
            dfs(next_n, inequal_idx+1, used + next_n)


if __name__ == "__main__":
    K = int(input())
    inequal_list = input().split()
    max_res, min_res = 0, 9876543211
    for start in map(str, range(10)):
        dfs(start, 0, start)
    if len(str(min_res)) != K+1:
        min_res = '0' + str(min_res)
    print(max_res, min_res, sep='\n')

