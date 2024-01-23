# 정수 삼각형

N = int(input())

DP = list(map(int, input().split()))  # 꼭대기

for _ in range(N-1):
    s = list(map(int, input().split()))
    s[0] += DP[0]
    for i in range(1, len(s)-1):
        if DP[i-1] < DP[i]:
            s[i] += DP[i]
        else:
            s[i] += DP[i-1]
    s[-1] += DP[-1]
    DP = s

print(max(DP))
