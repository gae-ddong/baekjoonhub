# 랜선 자르기

K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))

lan.sort()

end = lan[K-1]
start = 1
mid = 0

while start <= end:
    sum = 0
    mid = (start+end)//2

    for i in lan:
        sum += i//mid
    if sum < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)