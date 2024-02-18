# 양념 반 후라이드 반

A, B, C, X, Y = map(int, input().split())

if A + B > 2*C:
    if X > Y:
        print(min(2*C * X, Y * 2*C + A*(X-Y)))
    else:
        print(min(2*C * Y, X * 2*C + B*(Y-X)))
else:
    print(A*X + B*Y)
