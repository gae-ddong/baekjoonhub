import sys
from math import *
fn = int(sys.stdin.readline().rstrip())
mylist = [1, 2, 6, 24, 120, 720]
if fn in mylist:
    print(mylist.index(fn)+1)
else:
    l = int(log10(fn))+1
    num = 0
    count = 0
    while True:
        count += 1
        num += log10(count)
        if int(num)+1 == l:
            print(count)
            break