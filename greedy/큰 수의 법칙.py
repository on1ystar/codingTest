N, M, K = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
answer = 0
li.sort()
while True:
    for i in range(K):
        if M == 0: break
        answer += li[-1]
        M -= 1
    if M == 0: break
    answer += li[-2]
    M -= 1
print(answer)