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