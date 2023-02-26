# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 두 개의 숫자열

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    if n > m:
        n, m = m, n
        arr_1, arr_2 = arr_2, arr_1
    max_num = 0
    for i in range(m - n + 1):
        temp = 0
        for j in range(n):
            temp += arr_1[j] * arr_2[j + i]
        if max_num < temp:
            max_num = temp
    print(f"#{tc} {max_num}")
