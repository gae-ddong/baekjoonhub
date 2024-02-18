# 부등호

numh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numl = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

comp_num = []

k = int(input())
comp = list(input().split())


# 연속하는 부등호 개수 구해서 리스트로 만들기 ex) > < < < > > > < <
cnt = 0
start = comp[0]

for i in comp:
    if i == start:
        cnt += 1
    else:
        comp_num.append(cnt)
        cnt = 1
        start = i

comp_num.append(cnt)
# comp_num = [1,3,3,2]


max = []
min = []

s = 0 if comp[0] == '>' else 1

for i in range(len(comp_num)):
    if (i+s) % 2 == 0:
        for j in range(comp_num[i]):
            min.append(numh[comp_num[i]-j])
            del numh[comp_num[i]-j]
            max.append(numl[0])
            del numl[0]
    else:
        for j in range(comp_num[i]):
            min.append(numh[0])
            del numh[0]
            max.append(numl[comp_num[i]-j])
            del numl[comp_num[i]-j]

min.append(numh[0])
max.append(numl[0])

print(''.join(map(str, max)))
print(''.join(map(str, min)))
