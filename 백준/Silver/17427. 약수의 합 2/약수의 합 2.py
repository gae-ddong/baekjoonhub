# 약수의 합 2

N = int(input())
sum = (N+4)*(N-1)//2 + 1
i = 2
s = 4

while (s <= N):
    sum += i
    sum += i * (N//i - i) + (N//i - i)*(i+1+N//i)//2
    i += 1
    s = i * i

print(sum)
