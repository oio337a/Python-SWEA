# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 시각 덧셈

T = int(input())

for tc in range(1, T + 1):
    h_1, m_1, h_2, m_2 = map(int, input().split())

    h = h_1 + h_2
    m = m_1 + m_2

    if m >= 60:
        h += 1
        m -= 60
    if h > 12:
        h -= 12

    print("#{} {} {}".format(tc, h, m))
