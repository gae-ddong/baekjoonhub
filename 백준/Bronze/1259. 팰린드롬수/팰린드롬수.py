# 팰린드롬수

while (1):
    n = 0
    test = list(input())
    if test == ['0']:
        break
    for i in range(len(test)//2):
        if test[i] != test[-i-1]:
            n = 1
            break
    if n == 1:
        print("no")
    else:
        print("yes")
