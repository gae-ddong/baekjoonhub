# 문자열 반복

T = int(input())

for _ in range(T):
    token = input().split()
    R = int(token[0])
    str = list(token[1])
    for i in str:
        for _ in range(R):
            print(i, end="")
    print()