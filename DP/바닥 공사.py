N = int(input())
dp = [0] * (N + 1)
dp[1], dp[2] = 1, 3
for i in range(3,N+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 - 3
    else:
        dp[i] = dp[i-1] * 2 - 1

print(dp[N] % 796796)

d = [0] * (N + 1)
d[1], d[2] = 1, 3

for i in range(3, N+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[N])