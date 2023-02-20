# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QKsLaAy0DFAUq&categoryId=AV5QKsLaAy0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1

# 신문 헤드라인

text = input()

for i in text:
    if i >= "a" and i <= "z":
        print(chr(ord(i) - ord("a") + ord("A")), end="")
    else:
        print(i, end="")
