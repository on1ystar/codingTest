T = int(input())
d_col = [-1, -1, -1]  # 왼쪽 위, 왼쪽, 왼쪽 아래
d_row = [-1, 0, 1]
for _ in range(T):
    n, m = map(int, input().rstrip().split())
    li = list(map(int, input().rstrip().split()))
    mine = [li[i:i+n+1] for i in range(0,len(li),m)]  # 사실 만들 필요 없었음
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = mine[i][0]
    for col in range(1, m):
        for row in range(0, n):
            temp = []
            for i in range(3):
                if (0 <= (col + d_col[i]) < m) and (0 <= (row + d_row[i]) < n):
                    temp.append(dp[row + d_row[i]][col + d_col[i]])
            dp[row][col] = max(temp) + mine[row][col]
print(max([row[-1] for row in dp]))