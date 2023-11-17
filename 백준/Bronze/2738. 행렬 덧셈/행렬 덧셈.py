# 행렬 덧셈
N, M = map(int, input().split())
list1 = [0 for _ in range(N)]
list2 = [0 for _ in range(N)]

for i in range(N):
    list1[i] = list(map(int, input().split()))
for i in range(N):
    list2[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        list1[i][j] += list2[i][j]
for i in range(N):
    print(*list1[i])
