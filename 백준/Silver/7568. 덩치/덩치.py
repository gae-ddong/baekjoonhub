# 덩치

N = int(input())
X = []
Y = []
ans = [1 for i in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    X.append(a)
    Y.append(b)

for i in range(N):
    for j in range(N):
        if X[i] < X[j]:
            if Y[i] < Y[j]:
                ans[i] += 1

print(*ans)
