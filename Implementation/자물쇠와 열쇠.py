import copy

def rotation(m, copied_key):
    rotated_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated_key[j][m-i-1] = copied_key[i][j]
    return rotated_key

def init(n, lock, expanded_lock):
    for i in range(n):
        for j in range(n):
            expanded_lock[n+i][n+j] = lock[i][j]

def try_the_lock(start_i, start_j, m, n, key, expanded_lock):
    for i in range(m):
        for j in range(m):
            expanded_lock[start_i+i][start_j+j] += key[i][j]
    for i in range(n):
        for j in range(n):
            if expanded_lock[n+i][n+j] != 1:
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    answer = True
    expanded_lock = [[0] * (n * 3) for _ in range(n * 3)]
    init(n, lock, expanded_lock)
    for i in range(n):
        for j in range(n):
            if expanded_lock[n+i][n+j] != 1:
                answer = False
    if answer: return answer
    for _ in range(4):
        for i in range(n*2):
            for j in range(n*2):
                answer = try_the_lock(i, j, m, n, key, expanded_lock)
                if answer:
                    return answer
                init(m, lock, expanded_lock)
        key = rotation(m, copy.deepcopy(key))
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))