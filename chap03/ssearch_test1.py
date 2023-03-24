from ssearch_while import seq_search

print('실수를 검색합니다.')
print('End 입력 시, 프로그램 종료.')

number = 0
x = []

while True:
    s = input()
    if s == 'End':
        break
    x.append(float(s))
    
key  = float(input())

idx = seq_search(x,key)

if idx == -1 : 
    print('없습니다.')
else:
    print(f'위치 : {idx}')    