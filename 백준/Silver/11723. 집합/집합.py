# 집합
import sys

N = int(input())
s = 0

for _ in range(N):
    cal = list(sys.stdin.readline().split())
    if cal[0][1] == 'l':  # all
        s = 0b11111111111111111111
    elif cal[0][1] == 'm':  # empty
        s &= 0
    else:
        x = int(cal[1])-1
        if cal[0][0] == 'a':
            s |= (1 << x)
        elif cal[0][0] == 'r':
            s &= ~(1 << x)
        elif cal[0][0] == 'c':
            if s & (1 << x):
                print(1)
            else:
                print(0)
        else:  # toggle
            if s & (1 << x):
                s &= ~(1 << x)
            else:
                s |= (1 << x)
