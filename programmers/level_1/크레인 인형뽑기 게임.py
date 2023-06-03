# 방법 1
def solution(board, moves):
    answer = 0
    basket = []
    temp = [0]
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
    while True:
        if len(basket) == 0:
            break
        if basket[len(basket)-1] == temp[-1]:
            basket.pop()
            temp.pop()
            answer += 2
        else:
            temp.append(basket.pop())
    return answer

# 방법 2
# def solution(board, moves):
#     answer = 0
#     basket = [0]
#     for move in moves:
#         for i in range(len(board)):
#             if board[i][move-1] != 0:
#                 if board[i][move-1] == basket[-1]:
#                     answer += 2
#                     board[i][move-1] = 0
#                     basket.pop()
#                     break
#                 else:
#                     basket.append(board[i][move-1])
#                     board[i][move-1] = 0
#                     break
#     return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))