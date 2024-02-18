# 최대공약수와 최소공배수

a, b = map(int, input().split())
poss = []

for i in range(1, b+1):
    if a % i == 0 and b % i == 0:
        poss.append(i)

print(poss[-1])
print(a*b//poss[-1])
