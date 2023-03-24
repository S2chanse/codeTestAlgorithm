from typing import Any

class FixedStack:
    """고정길이의 스택 ㅋ르래스"""
    class Empty(Exception):
        """뺄깨 없다"""
        pass
    
    class Full(Exception):
        """가득 참"""
        pass

    def __init__(self,capacity:int = 256) -> None:
        """스탯 초기화"""
        self.stk = [None]*capacity
        self.capacity = capacity
        """포인터 현재 위치"""
        self.ptr = 0
    
    def __len__(self)->int:
        return self.ptr
    
    def is_empty(self)->bool:
        """스택이 비어 있는지 판단."""
        return self.ptr<=0
    
    def is_full(self)->bool:
        """스택이 가득 찾는지 판단"""
        return self.ptr>=self.capacity
    
    def push(self,value:Any)->None:
        """데이터 값을 입력한다."""
        if self.is_full(): #예외 발생-> 가득 차있을 경우
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr+=1
    
    def pop(self)->Any:
        """가장 마지막 값을 빼준다."""
        if self.is_empty(): #다 비었나?
            raise FixedStack.Empty        
        self.ptr -=1
        return self.stk[self.ptr]
    
    def peek(self)->Any:
        """스택의 가장 위 데이터 보기"""
        if self.is_empty(): #값이 없을 경우
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    def clear(self)->None:
        """스택 비움"""
        self.ptr = 0
    
    def find(self, value: Any)->int:
        if self.is_empty():#
            raise FileExistsError        
        for i in range(self.ptr -1,-1,-1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self,value: Any)->int:
        """스택에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c=+1
        return c
    
    def __contains__(self,value: Any)->bool:
        return self.count(value)>0
    
    def dump(self)-> None:
        """B to T 로 모든 데이터 출력"""
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])