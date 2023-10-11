list = []

N = int(input())

for i in range(1,1000000) :
    i = i + sum(map(int, str(i)))
    list.append(i)

if N in list :
    print(list.index(N)+1)
else :
    print(0)