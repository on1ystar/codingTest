# N과 M (3)
# from itertools import combinations

# N, M = map(int, input().rstrip().split())
# for p in list(map(" ".join, combinations(map(str, range(1, N+1)),M))):
#     print(p)


from sys import stdout


def main(permutation=[]):
    if len(permutation) == M:
        stdout.write(" ".join(permutation) + "\n")
        permutation.pop()
        return permutation
    for i in range(N):
        permutation.append(num_li[i])
        permutation = main(permutation)
    if permutation: 
        permutation.pop()
        return permutation
    

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    num_li = []
    num_li = list(map(str, range(1, N+1)))
    main()