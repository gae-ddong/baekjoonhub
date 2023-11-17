# 알고리즘 수업 - 점근적 표기 1
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1 < c and -a0/(a1-c) <= n0) or (a1 == c and a0 <= 0):
    print(1)
else:
    print(0)