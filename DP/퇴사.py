from sys import stdin
n = int(stdin.readline().rstrip())
tp = []
dp = [0] * n
for _ in range(n):
    tp.append(list(map(int, stdin.readline().rstrip().split())))
for i in range(n):
    temp = [0]
    for j in range(i):
        if i - j >= tp[j][0]:
            temp.append(dp[j])
    if n - i >= tp[i][0]:
        dp[i] = tp[i][1] + max(temp)
    else:
        dp[i] = max(temp)
print(max(dp))
