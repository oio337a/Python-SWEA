# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1

# 연월일 달력

t = int(input())

for i in range(t):
    arr = input()

    year = arr[:4]
    month = arr[4:6]
    day = arr[6:]

    last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(month) > 0 and int(month) < 13:
        if int(day) > 0 and int(day) <= last_day[int(month) - 1]:
            print(f"#{i+1} {year}/{month}/{day}")
            continue
    print(f"#{i+1} -1")
