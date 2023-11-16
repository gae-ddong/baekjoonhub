# Z

N, r, c = map(int, input().split())
answer = 0

for i in range(1, N+1):
    if 2**(N-i) > c:
        if 2**(N-i) > r:
            answer += 0
        else:
            answer += 2 ** (2*N-2*i)*2
            r -= 2**(N-i)
    else:
        if 2**(N-i) > r:
            answer += 2 ** (2*N-2*i)
            c -= 2**(N-i)
        else:
            answer += 2 ** (2*N-2*i)*3
            r -= 2**(N-i)
            c -= 2**(N-i)

if r == 0:
    if c == 0:
        answer += 0
    else:
        answer += 1
else:
    if c == 0:
        answer += 2
    else:
        answer += 3

print(answer)
