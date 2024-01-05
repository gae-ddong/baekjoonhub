# 1로 만들기

MAXNUM = 1000000

N = int(input())
DP = [0, 0, 1, 1]

for i in range(4, N+1):
    if (i % 2 == 0):
        div2 = DP[i//2]
    else:
        div2 = MAXNUM
    if (i % 3 == 0):
        div3 = DP[i//3]
    else:
        div3 = MAXNUM
    sub1 = DP[i-1]
    DP.append(min(div2, div3, sub1)+1)

print(DP[N])
