# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

# N: stages length, stages: users pos
from operator import itemgetter


def solution(N, stages):
    answer = []
    failure = {}
    for i in range(1, N+1):
        failure[i] = 0
    stages.sort()
    reach = 0
    for i in range(N, 0, -1):
        n_clear = 0
        if not stages: break
        while stages and stages[-1] == N+1:
            stages.pop()
            reach += 1
            continue
        while stages and i == stages[-1]:
            stages.pop()
            reach += 1
            n_clear += 1
        if reach != 0: failure[i] = n_clear / reach

    li = sorted(failure.items(), key=itemgetter(1), reverse=True)
    for x in li:
        answer.append(x[0])
    return answer

print(solution(2, [1,1,3,2,1,1]))