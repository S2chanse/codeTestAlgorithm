from typing import Any,Sequence

def bin_search(a:Sequence, key:Any)->int:
    pl = 0
    pr = len(a)-1
    while True:
        pc = (pl+pr)//2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc+1
        else:
            pr = pc-1
        if pl>pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input())
    x = [None] * num
    
    x = list(map(int, input().split()))
    
    x.sort()
    
    key = int(input())
    
    idx = bin_search(x,key)
    
    if idx == -1 :
        print('값 X')
    else:
        print(idx)
        