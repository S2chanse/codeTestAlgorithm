from typing import Any,MutableSequence

def reverse(a: MutableSequence)-> None : 
    n = len(a)
    for i in range(n//2):
        a[i],a[n-i-1] = a[n-i-1],a[i]
                