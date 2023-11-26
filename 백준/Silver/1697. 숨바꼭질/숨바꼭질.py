# 숨바꼭질
from collections import deque
import math
import sys
sys.setrecursionlimit(10**7)
children = []

N, K = map(int, input().split())
MAX = 100000
visit = [0] * (MAX+1)


def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(visit[x])
            break

        for j in (x-1, x+1, 2*x):
            if 0 <= j <= MAX and not visit[j]:
                visit[j] = visit[x] + 1
                q.append(j)


bfs()
