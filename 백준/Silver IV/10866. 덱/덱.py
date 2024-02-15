# 덱

from collections import deque
import sys

deq = deque()
play = []

N = int(input())

for i in range(N):
    play = list(sys.stdin.readline().split())
    if play[0][0] == 's':
        print(len(deq))
    elif play[0][0] == 'e':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif play[0][0] == 'p' and play[0][1] == 'u':
        if play[0][5] == 'f':
            deq.appendleft(int(play[1]))
        else:
            deq.append(int(play[1]))
    elif len(deq) == 0:
        print(-1)
    else:
        if play[0][0] == 'f':
            print(deq[0])
        elif play[0][0] == 'b':
            print(deq[-1])
        else:
            if play[0][4] == 'f':
                print(deq.popleft())
            else:
                print(deq.pop())
