# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1

# 평균값 구하기

t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    print("#", i+1, " ", round(sum(arr) / 10), sep='')
