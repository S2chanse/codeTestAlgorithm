#a부터 b까지 정수의 합 구하기1

print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('input a : '))
b = int(input('input b : '))

if a>b : 
    a,b = b,a
sum = 0;
for i in range(a,b):
    sum+= i
    print(f'{i} +',end=' ')

sum+=b
print(f'{b} = {sum}')
    
