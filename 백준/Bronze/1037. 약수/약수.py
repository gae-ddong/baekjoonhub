# 약수
count = int(input())
div = list(map(int, input().split()))

if len(div) == 1:
    print(div[0]**2)
else:
    div.sort()
    print(div[0]*div[len(div)-1])
