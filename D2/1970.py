# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 쉬운 거스름돈

money = [50_000,
         10_000,
         5_000,
         1_000,
         500,
         100,
         50,
         10]


T = int(input())

for tc in range(1, T + 1):
    change = [0] * len(money)
    pay = int(input())

    for i in range(len(money)):
        if pay >= money[i]:
            change[i] = pay // money[i]
            pay %= money[i]
    print(f"#{tc}")
    print(*change)
