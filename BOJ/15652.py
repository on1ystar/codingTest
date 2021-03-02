from sys import stdout
from itertools import combinations_with_replacement

# N, M = map(int, input().rstrip().split())
# for c in map(" ".join, combinations_with_replacement(map(str, range(1,N+1)), M)):
#     stdout.write(c + "\n")


def main(combi=[], start_i=0):
    if len(combi) == M:
        stdout.write(" ".join(combi) + "\n")
        combi.pop()
        return combi
    for i in range(start_i, N):
        combi.append(num_li[i])
        combi = main(combi, i)
    if combi: 
        combi.pop()
        return combi
    

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    num_li = []
    num_li = list(map(str, range(1, N+1)))
    main()