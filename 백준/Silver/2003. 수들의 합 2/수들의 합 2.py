import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cnt = 0
j = 0
sum = 0
i = 0

while not (i == N and sum < M):
    if sum < M:
        sum += A[i]
        i += 1
    if sum > M:
        sum -= A[j]
        j += 1
    elif sum == M:
        cnt += 1
        sum -= A[j]
        j += 1


print(cnt)
