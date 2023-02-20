# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1

# 몫과 나머지 출력하기

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    print(f"#{i+1} {a//b} {a%b}")
