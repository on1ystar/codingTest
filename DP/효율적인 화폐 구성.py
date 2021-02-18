N, M = map(int, input().rstrip().split())
currency = []
dp = [-1] * (M + 1)
dp[0] = 0
for _ in range(N):
    currency.append(int(input()))

for i in range(1,M+1):
    for c in currency:
        if dp[(i % c)] != -1:
            if dp[i] == -1:
                dp[i] = (i // c) + dp[i % c]
            else:
                dp[i] = min(dp[i], (i // c) + dp[i % c])
print(dp[M])