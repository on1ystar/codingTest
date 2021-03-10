# 뱀과 사다리 게임


from collections import deque


if __name__ == "__main__":
    N, M = map(int, input().split()) # 사디리, 뱀
    jump = list(range(107)) 
    for _ in range(N):
        s, e = map(int, input().split())
        jump[s] = e
    for _ in range(M):
        s, e = map(int, input().split())
        jump[s] = e
    visited = [0] * 107
    q = deque([1])
    while q:
        now_pos = q.popleft()
        if now_pos == 100:
            print(visited[now_pos])
            break
        for i in range(1, 7):
            next_pos = jump[now_pos + i]
            if visited[next_pos] == 0 and next_pos <= 100:
                visited[next_pos] = visited[now_pos] + 1
                q.append(next_pos)