# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 지그재그 숫자

T = int(input())

for t in range(1, T + 1):
    n = int(input())

    odd_numbers = [i for i in range(n + 1) if i % 2 != 0]
    even_numbers = [i for i in range(n + 1) if i % 2 == 0]
    print("#{} {}".format(t, sum(odd_numbers) - sum(even_numbers)))
