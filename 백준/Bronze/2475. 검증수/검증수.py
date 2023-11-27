# 검증수

own = list(map(int, input().split()))
sum = 0

for i in own:
    sum += i**2

print(sum % 10)
