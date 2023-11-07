# 교수가 된 현우
T = int(input())
fact = []


for _ in range(T):
    fact.append(int(input()))
for i in fact:
    count = 0
    five = 5
    while five < i:
        five *= 5
        count += i//five
    print(count + i//5)
