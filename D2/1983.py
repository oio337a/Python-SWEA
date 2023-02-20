# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 조교의 성적 매기기

T = int(input())

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for t in range(1, T + 1):
    n, check_student = map(int, input().split())

    scores = [list(map(int, input().split())) for _ in range(n)]

    student_score = [sum([mid * 0.35, final * 0.45, assignment * 0.2])
                     for mid, final, assignment in scores]

    count = len([i for i in student_score if i >
                student_score[check_student - 1]])
    grade_amount = n // 10

    print("#{} {}".format(t, grades[count // grade_amount]))
