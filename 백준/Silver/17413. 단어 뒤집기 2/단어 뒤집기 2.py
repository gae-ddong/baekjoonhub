# 단어 뒤집기2

word = list(input())

reverse = 1  # <>안에 있으면 0, <> 안에 없으면 1
rev_list = []  # 역정렬할 부분 리스트
ans = []  # 정답

for i in word:
    if i == '<':
        reverse = 0
        if len(rev_list) != 0:
            rev_list.reverse()
            ans = ans + rev_list
            rev_list = []
        ans.append(i)
    elif i == '>':
        reverse = 1
        ans.append(i)
    elif reverse == 1:
        if i == ' ':
            rev_list.reverse()
            ans = ans + rev_list
            ans.append(i)
            rev_list = []
        else:
            rev_list.append(i)
    elif reverse == 0:
        ans.append(i)
rev_list.reverse()
ans = ans + rev_list
print(''.join(ans))
