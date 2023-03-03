def sum_1ton(n):
    s=0
    while n>0:
        s +=n
        n -=1
    return s;
x = int(input("넣을 값 : "))
print(f"{x} 결과값 : {sum_1ton(x)}")    