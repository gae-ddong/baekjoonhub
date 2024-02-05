# 수들의 합
import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

sum = 0
cnt = 0

for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += A[j]
        if sum >= M:
            if sum == M:
                cnt += 1
            break

print(cnt)
