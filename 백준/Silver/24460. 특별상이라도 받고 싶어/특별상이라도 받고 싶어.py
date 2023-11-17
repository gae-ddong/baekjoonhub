# 특별상이라도 받고 싶어
import pprint

N = int(input())


def special(select, N):
    if N == 1:
        return select[0]
    find_second = []
    find_second.append(special([row[0:N//2]
                                for row in select[0:N//2]], N//2))
    find_second.append(special([row[N//2:N]
                                for row in select[0:N//2]], N//2))
    find_second.append(special([row[:N//2]
                                for row in select[N//2:N]], N//2))
    find_second.append(special([row[N//2:N]
                                for row in select[N//2:N]], N//2))

    find_second.sort()
    second = find_second[1]
    return second


select = [list(map(int, input().split())) for _ in range(N)]
answer = str(special(select, N))[1:-1]
print(answer)
