# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1
# 홀수만 더하기

import sys
input = sys.stdin.readline

t = int(input())

for k in range(t):
    arr = list(map(int, input().split()))

    result = 0
    for i in arr:
        if (i % 2 == 1):
            result += i
    print("#", k + 1, " ", result, sep='')
