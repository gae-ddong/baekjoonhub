# 모든 순열

N = int(input())
check = [0 for i in range(N)]
ans = []


def back(N):
    global ans 
    if len(ans) == N:
        print(*ans)
        return
    
    for i in range(1, N+1):
        if check[i-1] == 0:
            check[i-1] = 1
            ans.append(i)
            back(N)
            check[ans.pop()-1] = 0 
    return


back(N)