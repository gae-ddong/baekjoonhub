# 약수의 합 2

N = int(input())
sum = (N+4)*(N-1)//2 + 1
i = 2
s = 4

while (s <= N):
    sum += i
    for j in range(i*(i+1), N+1, i):
        if j % (i) == 0:
            sum += i + (j // i)
    i += 1
    s = i * i

print(sum)
