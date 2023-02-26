# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 날짜 계산기

T = int(input())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T + 1):
    m_1, d_1, m_2, d_2 = map(int, input().split())

    day = 0
    if m_1 == m_2:
        day = d_2 - d_1 + 1
        print(f"#{tc} {day}")
        continue
    day += days[m_1] - d_1 + 1
    for i in range(m_1 + 1, m_2):
        day += days[i]
    day += d_2
    print(f"#{tc} {day}")
