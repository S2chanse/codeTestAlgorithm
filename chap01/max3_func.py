def max(a,b,c):
    """입력 변수의 최댓값 구하기"""
    maximum = a
    if b>maximum : maximum = b
    elif c>maximum : maximum = c
    return maximum

print(f'max(3,2,1) = {max(3,2,1)}')
print(f'max(3,2,2) = {max(3,2,2)}')
print(f'max(1,2,1) = {max(1,2,1)}')
print(f'max(1,2,3) = {max(1,2,3)}')
