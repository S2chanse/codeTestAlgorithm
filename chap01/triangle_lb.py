#왼쪽 아래가 직각인 이등변 삼각형 구하기

print('왼쪽아래 직각 삼각형')

n = int(input('짧은 변의 길이를 입력하세요 : '))
for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end="")
    print("*"*(i+1))
    