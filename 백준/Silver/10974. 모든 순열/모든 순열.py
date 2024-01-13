# 모든 순열

N = int(input())
ans = []


def back(N):
    global ans
    if len(ans) == N:
        print(*ans)
        return
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            back(N)
            del ans[-1]
    return


back(N)
