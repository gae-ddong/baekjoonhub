# 프린터 큐
from collections import deque

testcase = int(input())


for _ in range(testcase):
    popcount = 0
    filenum, index = map(int, input().split())
    file = deque(map(int, input().split()))
    while (1):
        if max(file) != file[0]:
            file.append(file[0])
            file.popleft()
            if index == 0:
                index = len(file)-1
            else:
                index -= 1
        else:
            file.popleft()
            popcount += 1
            if index == 0:
                print(popcount)
                break
            else:
                index -= 1
