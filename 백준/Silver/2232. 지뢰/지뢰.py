# 지뢰

N = int(input())
mine = [0]
answer = []

for _ in range(N):
    mine.append(int(input()))

mine.append(0)

for i in range(1, N+1):
    if mine[i-1] <= mine[i] and mine[i] >= mine[i+1]:
        answer.append(i)

for i in answer:
    print(i)
