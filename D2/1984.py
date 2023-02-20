# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 중간 평균값 구하기

T = int(input())


for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    print("#{} {}".format(t, round(sum(arr[1:9]) / 8)))
