# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

# 달팽이 숫자

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    board = [[0] * n for _ in range(n)]

    num = 0
    for i in range(n // 2):
        turn = ((n - 1) - 2 * i)
        for j in range(turn):
            board[i][i + j] = num + j + 1
            board[i + j][(n - 1) - i] = num + (turn) + (j + 1)
            board[(n - 1) - i][(n - 1) - (i + j)] = num + 2 * (turn) + (j + 1)
            board[(n - 1) - (i + j)][i] = num + 3 * (turn) + (j + 1)
        num += 4 * (turn)
    if n % 2 == 1:
        board[n // 2][n // 2] = n**2
    print(f'#{tc}')
    for lines in range(n):
        print(*board[lines])
