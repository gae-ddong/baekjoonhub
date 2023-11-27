# 알파벳 찾기

str = list(input())
loc = [-1]*26
index = 0

for i in str:
    if loc[ord(i)-97] == -1:
        loc[ord(i)-97] = index
    index += 1

print(*loc)
