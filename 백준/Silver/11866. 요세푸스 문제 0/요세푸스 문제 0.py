# 요세푸스 문제 0

N, K = map(int, input().split())

list = list(range(1, N+1))  # 1~N 요소 가지는 0~N-1 인덱스 리스트
i = K-1

print("<", end="")

while True:
    print(list[i], end="")
    list.remove(list[i])
    if len(list) == 0:
        break
    i = (i + K-1) % len(list)
    print(", ", end="")

print(">", end="")
