# 단어 뒤집기2

word = list(input())

reverse = 1  # <>안에 있으면 0, <> 안에 없으면 1
rev_list = []  # 역정렬할 부분 리스트

for i in word:
    if i == '<':
        reverse = 0
        if len(rev_list) != 0:
            rev_list.reverse()
            print(''.join(rev_list), end="")
            rev_list = []
        print(i, end="")
    elif i == '>':
        reverse = 1
        print(i, end="")
    elif reverse == 1:
        if i == ' ':
            rev_list.reverse()
            print(''.join(rev_list), end="")
            rev_list = []
            print(i, end="")
        else:
            rev_list.append(i)
    elif reverse == 0:
        print(i, end="")
rev_list.reverse()
print(''.join(rev_list), end="")
