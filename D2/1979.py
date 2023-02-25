# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 어디에 단어가 들어갈 수 있을까

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())

    arr = [input().split() for _ in range(n)]
    temp_1 = [''.join(arr[i]).split('0') for i in range(n)]
    temp_2 = [''.join(i).split('0') for i in list(zip(*arr))]

    count = 0
    for i in temp_1:
        for j in i:
            if j.count('1') == k:
                count += 1
    for i in temp_2:
        for j in i:
            if j.count('1') == k:
                count += 1
    print("#{} {}".format(tc, count))
