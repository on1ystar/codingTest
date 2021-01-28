s = input()
result = int(s[0])
for x in s[1:]:
    result = max(result*int(x), result+int(x))
print(result)