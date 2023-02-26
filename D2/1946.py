# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PmkDKAOMDFAUq&categoryId=AV5PmkDKAOMDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 간단한 압축 풀기

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = input().split()
        arr.append((a, int(b)))
    count = 0
    print(f"#{tc}")
    for i in arr:
        for j in range(i[1]):
            print(i[0], end='')
            count += 1
            if count == 10:
                count = 0
                print()
    print()
