# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

#  파스칼의 삼각형

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    board[0][0] = 1

    for j in range(1, n):
        for k in range(0, j + 1):
            if k == 0 or k == j:
                board[j][k] = 1
            else:
                board[j][k] = board[j - 1][k - 1] + board[j - 1][k]
    print("#", i, sep="")
    for x in board:
        for y in x:
            if y != 0:
                print(y, end=" ")
        print()
