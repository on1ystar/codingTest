ch = input()
pos = [int(ch[1]), 1]
cnt = 0
def inner_check(row, col):
    if (1 <= row <= 8) and (1 <= col <= 8):
        return True
    else:
        return False
if ch[0] == 'a': pos[1] = 1
elif ch[0] == 'b': pos[1] = 2
elif ch[0] == 'c': pos[1] = 3
elif ch[0] == 'd': pos[1] = 4
elif ch[0] == 'e': pos[1] = 5
elif ch[0] == 'f': pos[1] = 6
elif ch[0] == 'g': pos[1] = 7
elif ch[0] == 'h': pos[1] = 8
if inner_check(pos[0]+2, pos[1]+1): cnt += 1
if inner_check(pos[0]+2, pos[1]-1): cnt += 1
if inner_check(pos[0]-2, pos[1]+1): cnt += 1
if inner_check(pos[0]-2, pos[1]-1): cnt += 1
if inner_check(pos[0]+1, pos[1]+2): cnt += 1
if inner_check(pos[0]+1, pos[1]-2): cnt += 1
if inner_check(pos[0]-1, pos[1]+2): cnt += 1
if inner_check(pos[0]-1, pos[1]-2): cnt += 1
print(cnt)