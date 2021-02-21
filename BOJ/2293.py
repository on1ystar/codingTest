from sys import stdin

N, K = map(int, input().rstrip().split())
coins = []
dp = [0] * (K+1)
dp[0] = 1
for _ in range(N):
    coins.append(int(stdin.readline().rstrip()))
coins.sort()

for coin in coins:
    for i in range(1, K+1):
        if i//coin == 0:
            continue
        dp[i] += dp[i - coin]
    print(f'coin={coin}:', dp)
print(dp[K])