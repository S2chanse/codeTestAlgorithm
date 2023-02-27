print("세 정수의 최댓값을 구합니다.")
#순차 구조
a=int(input('정수 a의 값을 입력하세요.:'))
b=int(input('정수 b의 값을 입력하세요.:'))
c=int(input('정수 c의 값을 입력하세요.:'))

maximum = a;
#선택 구조
if b>maximum: maximum = b
if c>maximum: maximum = c
print(f'최댓값은 {maximum}입니다.');