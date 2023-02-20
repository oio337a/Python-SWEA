# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 간단한 369게임

n = int(input())

for i in range(1, n + 1):

    i = str(i)
    check_num = i.count('3') + i.count('6') + i.count('9')

    if check_num == 0:
        print(i, end=' ')
    else:
        print('-' * check_num, end=' ')
