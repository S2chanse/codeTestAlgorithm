from max import max_of

print("배열의 최댓값 구하기")
print('End 입력 시, 종료')

number = 0
x = []
while True:
    s = input(f'x[{number}]값을 입력하세요.')
    if s == 'End' : 
        break        
    x.append(int(s))
    number+=1

print(f'x의 갯수는 {number}이고, 최댓값은 {max_of(x)}입니다.')
    