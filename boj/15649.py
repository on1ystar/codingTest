# N과 M (1)

# from itertools import permutations

# N, M = map(int, input().rstrip().split())
# for p in list(map(" ".join, permutations(map(str, range(1, N+1)),M))):
#     print(p)



def permu(now_permu=[]):
    if len(now_permu) == M:
        print(" ".join(now_permu))
        now_permu.pop()
        return now_permu
    for i in range(N):
        if li[i] not in now_permu: now_permu.append(li[i])
        else: continue
        now_permu = permu(now_permu)
    return now_permu[:-1]

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    li = list(map(str, range(1,N+1)))
    permu()