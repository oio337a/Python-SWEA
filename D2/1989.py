# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 초심자의 회문 검사

T = int(input())

for t in range(1, T + 1):
    text = input().strip()
    l = len(text)
    result = 1
    for i in range(l // 2):
        if text[i] != text[l - i - 1]:
            result = 0
            break
    print("#{} {}".format(t, result))
