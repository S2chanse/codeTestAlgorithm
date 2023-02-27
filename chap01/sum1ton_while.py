#1부터 n까지 합 구하기

print('1부터 n까지 합을 구합니다.')
n=int(input('n값을 입력해주세요'))
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print(f'1부터 {n}까지의 합은 {sum}입니다.');