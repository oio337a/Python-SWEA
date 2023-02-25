# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 숫자 배열 회전

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr = [list(map(str, input().split())) for _ in range(n)]
    arr_90 = [i[::-1] for i in zip(*arr)]
    arr_180 = [i[::-1] for i in arr[::-1]]
    arr_270 = [i for i in zip(*arr)][::-1]
    print(f"#{tc}")
    for i in range(n):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))
