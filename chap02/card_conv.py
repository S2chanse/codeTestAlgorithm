def card_conv(x: int,r:int)->str:
    d=''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTRVWXYZ'
    
    while x>0:
        d += dchar[x%r]
        x//=r
    return d[::-1]
if __name__=='__main__':
    print('10 진수 to n진수')
    while True:
        while True: #음이 아닌 정수 체크
            no = int(input("변환활 값으로 음이 아닌 정수를 입력하세요: "))
            if no>0:
                break
        while True:
            cd = int(input("진수를 선택해 주세요. : "))
            if 2<=cd<=36:
                break
        print(f'{no}를 {cd}진법으로 바꾼 결과 {card_conv(no,cd)}')
        
        retry = input("한 번 더 변환? Y : N :")
        if retry in {'N','n'}:
            break
            
