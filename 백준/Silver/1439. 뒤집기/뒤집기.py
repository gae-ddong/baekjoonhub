# 뒤집기

test = list(map(int, list(input())))

num = [0, 0]

for i in range(len(test)-1):
    if test[i] != test[i+1]:
        num[test[i]] += 1
num[test[-1]] += 1

print(min(num))