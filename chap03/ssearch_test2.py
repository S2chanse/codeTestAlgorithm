from ssearch_while import seq_search

print('실수를 검색합니다.')
print('End 입력 시, 프로그램 종료.')

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS','AAC','FLAC']

print(f'{s}에서 "n"의 인덱스는 {seq_search(s,"n")}') 