# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1
# 큰 놈, 작은 놈, 같은 놈

t = int(input())
for i in range(t):
    a, b = map(int, input().split())

    result = ""
    if a > b:
        result = ">"
    elif a < b:
        result = "<"
    else:
        result = "="
    print("#", i+1, " ", result, sep='')
