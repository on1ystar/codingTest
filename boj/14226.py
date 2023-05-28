# 이모티콘

from collections import deque

S = int(input())
dp = [[0] * 1001 for _ in range(1001)]  # 시간 저장
q = deque([(1, 0)])
while q:
    display, clip = q.popleft()
    if display == S:
        print(dp[display][clip])
        break
    now = dp[display][clip]
    if display < S:
        if dp[display][display] == 0: 
            dp[display][display] = now + 1
            q.append((display, display))
    if display + clip < 1001 and clip != 0:
        if dp[display + clip][clip] == 0: 
            dp[display + clip][clip] = now + 1
            q.append((display+clip, clip))
    if display > 2:
        if dp[display-1][clip] == 0: 
            dp[display-1][clip] = now + 1
            q.append((display-1, clip))