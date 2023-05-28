# 1, 2, 3 더하기

def counting(n):
    if n == 0:
        global result
        result = result + 1
        return
    if n-3 >= 0:
        counting(n-3)
    if n-2 >= 0:
        counting(n-2)
    counting(n-1)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        result = 0
        n = int(input())
        counting(n)
        print(result)