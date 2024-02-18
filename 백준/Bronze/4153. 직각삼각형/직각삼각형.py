# 직각삼각형

while (1):
    test = list(map(int, input().split()))
    if sum(test) == 0:
        break
    else:
        test.sort()
        if test[2]**2 == test[0]**2+test[1]**2:
            print("right")
        else:
            print("wrong")
