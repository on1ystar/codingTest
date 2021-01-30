import operator
from collections import deque


def solution(food_times, k):
    answer = 0
    food_times_dic = {}
    for i, v in enumerate(food_times):
        food_times_dic[i+1] = v
    sorted_dic_q = deque(sorted(map(list, food_times_dic.items()), key=operator.itemgetter(1)))

    while True:
        n = k // len(sorted_dic_q)
        if n >= 1:
            iter_cnt = min(sorted_dic_q[0][1], n)
            k -= len(sorted_dic_q) * iter_cnt
            for food in sorted_dic_q:
                food[1] -= iter_cnt
            while True:
                if food_times_dic == {}:
                    return -1
                if sorted_dic_q[0][1] == 0:
                    i, _ = sorted_dic_q.popleft()
                    del food_times_dic[i]
                else:
                    break
        else:
            answer = sorted(food_times_dic.items(), key=operator.itemgetter(0))[k][0]
            break
    return answer


print(solution([3, 1, 2, 1 ,2, 3, 4 ,5, 4, 6 ,7], 11))
