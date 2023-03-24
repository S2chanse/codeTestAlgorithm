from __future__ import annotations
from typing import Any,Type
import hashlib

class Node:
    """해시를 구성하는 노드"""
    
    def __init__(self,key:Any, value:Any,next:Node) -> None:
        """초기화"""
        self.key = key      #키
        self.value = value  #값
        self.next = next    #뒤쪽 노드 참조

class LinkedList:
    def __init__(self,capacity:int) -> None:
        self.capacity = capacity            
        self.table = [Node]*self.capacity
        