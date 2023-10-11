five = 0
two = 0
n = int(input())
five = n // 5
rest = n - five * 5
if rest % 2 == 0:
    two = rest // 2
else:
    rest = rest + 5
    five = five - 1
    two = rest // 2
if n == 1 or n == 3 :
    print(-1)
else :
    print(five+two)
