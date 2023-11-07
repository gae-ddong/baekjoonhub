# 치킨 TOP N
import copy

N = int(input())
upper = list(map(int, input().split()))
K = int(input())
temp = []
answer = []

for i in range(K):
    temp = copy.deepcopy(upper[i*N//K: (i+1)*N//K])
    temp.sort()
    answer.extend(temp)
print(*answer)
