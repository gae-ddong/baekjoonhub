# 유기농 배추

import sys
sys.setrecursionlimit(10**7)


def adjList(farm, nod1, nod2):
    farm[nod1][nod2] = 0
    if farm[nod1-1][nod2] == 1:
        adjList(farm, nod1-1, nod2)
    if farm[nod1+1][nod2] == 1:
        adjList(farm, nod1+1, nod2)
    if farm[nod1][nod2-1] == 1:
        adjList(farm, nod1, nod2-1)
    if farm[nod1][nod2+1] == 1:
        adjList(farm, nod1, nod2+1)
    if farm[nod1-1][nod2] == 0 and farm[nod1+1][nod2] == 0 and farm[nod1][nod2-1] == 0 and farm[nod1][nod2+1] == 0:
        return 1


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = []
    worm = 0

    farm = [[0]*(M+2) for _ in range(N+2)]

    for _ in range(K):
        a, b = map(int, input().split())
        farm[b+1][a+1] = 1

    for i in range(1, N+1):
        for j in range(1, M+1):
            if farm[i][j] == 1:
                worm += 1
                adjList(farm, i, j)
    print(worm)
