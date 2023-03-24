from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])

def select_menu()->Menu:
    """메뉴선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ',end='')
        
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)    

while True:
    print(f'현재 데이터 개수 : {len(s)}/{s.capacity}')
    menu = select_menu() # 메뉴선택
    
    if menu == Menu.푸시: #푸시
        x = int(input('데이터를 입력하세요. : '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 찼습니다.')
    elif menu == Menu.팝: #팝
        try:
            x = s.pop()
            print(f'{x}값이 팝됐습니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    elif menu == Menu.피크: #피크
        try:
            x = s.peek()
            print(f'{x}값이 최상위 값입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')  
    elif menu == Menu.검색: #검색하기
        x = int(input())
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('찾을 수 없습니다.')      
    elif menu == Menu.덤프 : #덤프
        s.dump()
    
    else:
        break
    