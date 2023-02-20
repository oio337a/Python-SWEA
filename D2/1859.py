# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
#  백만 장자 프로젝트

t = int(input())

for i in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    pay = 0
    max_num = 0
    for j in range(n - 1, -1, -1):
        if stock[j] > max_num:
            max_num = stock[j]
        else:
            pay += max_num - stock[j]
    print(f"#{i + 1} {pay}")
