# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1

# 1대1 가위바위보

a, b = map(int, input().split())

if a == 1 and b == 3:
    print("A")
elif a == 3 and b == 1:
    print("B")
elif a < b:
    print("B")
else:
    print("A")
