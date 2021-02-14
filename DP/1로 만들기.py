X = int(input())
dp = [0] * (X * 5 + 1)
dp[2], dp[3], dp[5] = 1, 1, 1
nums = [2, 3, 5]
if X == 1:
    print(0)
for i in range(2,X+1):
    for n in nums:
        temp = i * n
        if dp[temp] != 0 and (dp[temp] < (dp[i] + 1)):
            continue
        else:
            dp[temp] = dp[i] + 1
    temp = i+1
    if dp[temp] != 0 and (dp[temp] < (dp[i] + 1)):
        continue
    else:
        dp[temp] = dp[i] + 1
print(dp[X])
