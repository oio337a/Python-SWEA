# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 패턴 마디의 길이
case_count = int(input())

for i in range(1, case_count + 1):
    string = input()
    word = ''
    for char in string:
        word += char
        length = len(word)
        if word == string[length:length+length]:
            rest_string = string[length:]
            rest_string = rest_string.replace(word, '')
            if len(rest_string) < len(word):
                break
    print('#{} {}'.format(i, len(word)))
