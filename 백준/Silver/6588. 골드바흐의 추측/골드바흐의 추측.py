# 골드바흐의 추측
import sys

list = [1 for i in range(1000000+1)]
possible = 0

for i in range(2, 1000+1):
    if list[i]:
        j = 2
        while i * j <= 1000000:
            list[i*j] = 0
            j += 1

while (1):
    N = int(sys.stdin.readline())
    if N == 0:
        break
    else:
        if list[2] == 1 and list[N - 2] == 1:
            print(f"{N} = 2 + {N-2}")
            possible = 1
        else:
            for i in range(3, 1000+1, 2):
                if list[i] == 1 and list[N - i] == 1:
                    print(f"{N} = {i} + {N-i}")
                    possible = 1
                    break

if possible == 0:
    print("Goldbach's conjecture is wrong.")
