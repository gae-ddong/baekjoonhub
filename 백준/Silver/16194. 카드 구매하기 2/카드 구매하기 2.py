# 카드 구매하기2

N = int(input())

DP = list(map(int, input().split()))
possible = []

for i in range(N):
    for j in range((i+1)//2):
        possible.append(DP[j]+DP[i-j-1])
    possible.append(DP[i])
    DP[i] = min(possible)
    possible = []

print(DP[-1])
