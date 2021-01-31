def rotation(d):
    if d == 0: return 3
    elif d == 1: return 0
    elif d == 2: return 1
    else: return 2

def check(a, b, d, my_map):
    if d == 0 and (0 <= b-1):
        return my_map[a][b-1]
    elif d == 1 and (0 <= a-1):
        return my_map[a-1][b]
    elif d == 2 and (b+1 < m):
        return my_map[a][b+1]
    elif d == 3 and (a+1 < n):
        return my_map[a+1][b]
    else:
        return False

def forward(a, b, d):
    if d == 0: return [a-1 , b]
    elif d == 1: return [a, b+1]
    elif d == 2: return [a+1, b]
    else: return [a, b-1]

def back(a, b, d):
    if d == 0 and (a+1 < n): return [a+1, b]
    elif d == 1 and (0 <= a-1): return [a, b-1]
    elif d == 2 and (0 <= a-1): return [a-1, b]
    elif d == 3 and (b+1 < m): return [a, b+1]
    else: False

n, m = map(int, input().rstrip().split())
a, b, d = map(int, input().rstrip().split())
my_map = []
for _ in range(n):
    my_map.append(list(map(int, input().rstrip().split())))
my_map[a][b] = -1
rotation_cnt = 0
visit_cnt = 1
while True:
    checked = check(a, b, d, my_map)
    if checked == 0:
        d = rotation(d)
        a, b = forward(a, b, d)
        my_map[a][b] = -1
        visit_cnt += 1
        rotation_cnt = 1
        continue
    else:
        d = rotation(d)
        rotation_cnt += 1
    if rotation_cnt == 4:
        back_pos = back(a, b, d)
        if back_pos == False or my_map[back_pos[0]][back_pos[1]] == 1:
            break
        else:
            a, b = back_pos
            rotation_cnt = 1
print(visit_cnt)
