# 단어 공부

str = list(input())
alpha = [0]*26

for i in str:
    if ord(i) >= 97:
        alpha[ord(i)-97] += 1
    else:
        alpha[ord(i)-65] += 1

if alpha.count(max(alpha)) > 1:
    print("?")
else:
    print(chr(alpha.index(max(alpha))+65))
