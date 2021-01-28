s = input()
diff = False
cnt = 0
while True:
    if diff == True:
        if x == '0':
            s = s[:start] + '1'* (len(s) - start)
        else:
            s = s[:start] + '0'* (len(s) - start)
        cnt += 1
    init = s[0]
    start = 0
    x = ''
    diff = False
    for i, x in enumerate(s[:]):
        if init != x:
            if diff == True:
                s = s[0:start] + (x*(i-start)) + s[i:]
                cnt += 1
                init = s[i]
                start = i
                diff = False
            else:
                diff = True
                init = s[i]
                start = i
    if s == '0'*len(s) or s == '1'*len(s):
        break
print(cnt)