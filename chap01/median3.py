#세 정수를 입력받아 중앙값 구하기 1
def med3(a,b,c):
    """a,b,c의 중앙값 구하여 반환"""
    if a >= b:
        if b>=c: 
            return b;
        elif a<=c:
            return a;
        else : return c;
    elif a>c: return a;
    elif b>c: return c;
    else: return b;    
        
print('세 정수의 중앙값을 구합니다.')
a=int(input('a를 입력해 주세요.'))
b=int(input('b를 입력해 주세요.'))
c=int(input('c를 입력해 주세요.'))

print(f'a,b,c, 중앙값은 {med3(a,b,c)} 입니다.')