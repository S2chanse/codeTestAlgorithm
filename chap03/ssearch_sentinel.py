from typing import Any, Sequence
import copy

def seq_search(seq:Sequence,key:Any)->int:
    
    i = 0
    a = copy.deepcopy(seq)
    a.append(key)
    while True:
        if a[i] == key:
            break
        i+=1
    return -1 if i == len(seq) else i
    
if __name__ == '__main__':
    num = int(input('원소 수를 입력하시오 : '))
    
    x = [None] * num
    for i in range(num):
        x[i]  = int(input())
        
    key = int(input('검색 key :'))
    idx = seq_search(x,key)
    
    if idx == -1 :
        print('값을 찾지 못함')
    else:
        print(f'{key}는 {idx} 번쨰에 있다.')
        
    