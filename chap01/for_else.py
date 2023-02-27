import random
# 난수 생성 => 13 나오면 중단
n=int(input('난수 개수 : '))

for _ in range(n):
    r=random.randint(10,99)
    print(r,end=" ")
    if r == 13: 
        print('\rn 프로그램을 종료합니다.')
        break
else: 
    print("난수 생성을 중단합니다.")
