# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1
# 최대수 구하기

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))

    arr.sort()
    print("#", i+1, " ", arr[-1], sep='')
