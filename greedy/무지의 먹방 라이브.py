# import operator
# from collections import deque


# def solution(food_times, k):
#     answer = 0
#     food_times_dic = {}
#     for i, v in enumerate(food_times):
#         food_times_dic[i+1] = v
#     sorted_dic_q = deque(sorted(map(list, food_times_dic.items()), key=operator.itemgetter(1)))
#     while True:
#         n = k // len(sorted_dic_q)
#         if n >= 1:
#             iter_cnt = min(sorted_dic_q[0][1], n)
#             k -= len(sorted_dic_q) * iter_cnt
#             for food in sorted_dic_q:
#                 food[1] -= iter_cnt
#             while True:
#                 if food_times_dic == {}:
#                     return -1
#                 if sorted_dic_q[0][1] == 0:
#                     i, _ = sorted_dic_q.popleft()
#                     del food_times_dic[i]
#                 else:
#                     break
#         else:
#             answer = list(food_times_dic.items())[k][0]
#             break
#     return answer

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    food_times_dic = {}
    for i, v in enumerate(food_times):
        food_times_dic[i+1] = v
    while True:
        iter_cnt = k // len(food_times_dic)
        if iter_cnt >= 1:
            for key, time in list(food_times_dic.items()):
                temp = time - iter_cnt
                if temp <= 0:
                    k -= iter_cnt + temp
                    del food_times_dic[key]
                else:
                    k -= iter_cnt
                    food_times_dic[key] = temp
        else:
            answer = list(food_times_dic.items())[k][0]
            break
    return answer

print(solution([3, 1, 2], 6))
