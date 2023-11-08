# 암기왕

T = int(input())


def binarySearch(note, a):
    start = 0
    end = len(note) - 1

    while start <= end:
        mid = (start+end)//2

        if note[mid] == a:
            return 1
        elif note[mid] < a:
            start = mid + 1
        else:
            end = mid - 1

    return 0


for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()
    for i in note2:
        print(binarySearch(note1, i))