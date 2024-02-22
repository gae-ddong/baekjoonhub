# 십자가 찾기
import sys
import copy

N, M = map(int, sys.stdin.readline().split())
square = [['0' for _ in range(M)] for _ in range(N)]


cnt = 0
ans = []

for i in range(N):
    square[i] = list(sys.stdin.readline())[:-1]

delete = copy.deepcopy(square)

for x in range(1, N-1):
    for y in range(1, M-1):
        for s in range(1, (min(N, M)-1)//2+1):
            if x-s < 0 or y-s < 0 or x+s >= N or y+s >= M:
                break
            if square[x][y] == '*' and square[x-s][y] == '*' and square[x][y-s] == '*' and square[x][y+s] == '*' and square[x+s][y] == '*':
                cnt += 1
                ans.append([x+1, y+1, s])
                delete[x][y] = '.'
                delete[x-s][y] = '.'
                delete[x][y-s] = '.'
                delete[x+s][y] = '.'
                delete[x][y+s] = '.'
            else:
                break


if any('*' in l for l in delete):
    print(-1)
else:
    print(cnt)
    for i in range(cnt):
        print(*ans[i])
