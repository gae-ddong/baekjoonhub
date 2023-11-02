# 실버 V

N = int(input())
list = list(range(1, N+1))

while True:
    print(list[0], end=" ")
    list.remove(list[0])
    if len(list) == 0:
        break
    list.append(list[0])
    list.remove(list[0])
