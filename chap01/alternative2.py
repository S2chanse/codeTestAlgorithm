#+와 - 번갈아 추력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력 할까요?:'))

for _ in range(n//2):
    print("+-",end="");
  
if n%2:
    print("+");

        