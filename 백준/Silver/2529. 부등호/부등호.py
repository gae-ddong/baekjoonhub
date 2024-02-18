import sys
num_high = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_low = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
k = int(input())
comp = list(sys.stdin.readline().split())
comp_num = []
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
max = []
min = []
s = 0 if comp[0] == '>' else 1
for i in range(len(comp_num)):
    if (i+s) % 2 == 0:
        for j in range(comp_num[i]):
            min.append(num_high[comp_num[i]-j])
            del num_high[comp_num[i]-j]
            max.append(num_low[0])
            del num_low[0]
    else:
        for j in range(comp_num[i]):
            min.append(num_high[0])
            del num_high[0]
            max.append(num_low[comp_num[i]-j])
            del num_low[comp_num[i]-j]
min.append(num_high[0])
max.append(num_low[0])
print(''.join(map(str, max)))
print(''.join(map(str, min)))
