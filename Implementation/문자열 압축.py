def solution(s):
    if s == "":
        return 0
    if len(s)//2+1 == 1:
        return 1
    answer = []
    for i in range(1, len(s)//2+1):
        s_comp = []
        j = 0
        cnt = 1
        while j+i+i <= len(s):
            if s[j:j+i] == s[j+i:j+i+i]:
                cnt += 1
                j += i
            else:
                if cnt == 1:
                    s_comp.append(s[j:j+i])
                    j += i
                else:
                    s_comp.append(str(cnt))
                    s_comp.append(s[j:j+i])
                    j += i
                    cnt = 1
        if cnt == 1:
            s_comp.append(s[j:])
        else:
            s_comp.append(str(cnt))
            s_comp.append(s[j:j+i])
            if j+i < len(s):
                s_comp.append(s[j+i:])
        answer.append(len(''.join(s_comp)))
    return min(answer)