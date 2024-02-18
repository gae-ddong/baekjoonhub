# 이항 계수1

N, K = map(int, input().split())
sum = 1

for i in range(N-K+1, N+1):
    sum *= i

for i in range(1, K+1):
    sum //= i

print(sum)
