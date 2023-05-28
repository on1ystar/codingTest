# 숨바꼭질 4

from collections import deque


if __name__ == "__main__":
    N, K = map(int, input().split())
    if N > K:
        print(N-K)
        for x in range(N, K-1, -1):
            print(x, end=" ")
    elif N == K:
        print(0, N, sep="\n")
    else:
        queue = deque([(N, [N])])
        visited = [False] * 100001
        t = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                now_pos, path = queue.popleft()
                if now_pos == K:
                    print(t)
                    print(" ".join(map(str, path)))
                    break
                if visited[now_pos]: continue
                visited[now_pos] = True
                if 0 < (now_pos * 2) < (2*K - now_pos) and (now_pos * 2) <= 100000:
                    queue.append((now_pos * 2, path + [now_pos * 2]))
                if (now_pos + 1) <= K:
                    queue.append((now_pos + 1, path + [now_pos + 1]))
                if (now_pos - 1) >= 0: 
                    queue.append((now_pos - 1, path + [now_pos - 1]))
            else:
                t += 1
                continue
            break