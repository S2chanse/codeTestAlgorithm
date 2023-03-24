from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu',['인큐','디큐','피크','검색','덤프','종료'])

def select_menu()->Menu:
    """메뉴선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ',end='')
        
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)    

while True:
    print(f'현재 데이터 개수 : {len(q)}/{q.capacity}')
    menu = select_menu() #메뉴 선택
    if menu == Menu.인큐: #인큐
        x = int(input('인큐할 데이터를 입력하세요 :  '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 다 찼습니다.')
    elif menu == Menu.디큐: #디큐
        try:
            x = q.deque()
            print(f'{x}가 디큐 됐습니다.')
        except FixedQueue.Empty:
            print('큐가 비어 있습니다.') 
    elif menu == Menu.피크 :
        try:
            x = q.peek()
            print(f'{x}가 피크 값입니다.')
        except FixedQueue.Empty:
            print('큐가 비어 있습니다.') 
    elif menu == Menu.검색: #피크
            x = int(input())
            if x in q:
                print(f'{q.find(x)}가 맨앞 값이고 동일 갯수 {q.count(x)}개입니다.')    
    elif menu == Menu.덤프: #덤프
            q.dump()
    else:
        break