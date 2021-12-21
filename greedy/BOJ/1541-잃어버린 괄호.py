# num_exp = input()
# new_num_exp = '('
# str_num = ''
# for c in num_exp:
#     if c == '-':
#         new_num_exp += str(int(str_num))
#         str_num = ''
#         new_num_exp += ')' + '-' + '('
#     elif c == '+':
#         new_num_exp += str(int(str_num)) + '+'
#         str_num = ''
#     else:
#         str_num += c
# if str_num != '':
#     new_num_exp += str(int(str_num))
# new_num_exp += ')'
# print(eval(new_num_exp))

li = input().split('-')
result = sum(list(map(int, li[0].split('+'))))
for e in li[1:]:
    result += (-1) * sum(list(map(int, e.split('+'))))
print(result)