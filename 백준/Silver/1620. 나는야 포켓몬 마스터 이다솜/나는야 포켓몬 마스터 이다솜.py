# 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())
dogam = {}

for i in range(N):
    dogam[i] = input()


dogam_reverse = {}
for k, v in dogam.items():
    dogam_reverse[v] = k

for _ in range(M):
    find = input()
    if find.isdigit():
        print(dogam[int(find)-1])
    else:
        print(dogam_reverse[find]+1)