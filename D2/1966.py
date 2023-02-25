# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 숫자를 정렬하자

T = int(input())

for tc in range(1, T + 1):
    input()
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{tc}", end=" ")
    print(*arr)
