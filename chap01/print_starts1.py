n = int(input('몇 개 출력?:'))
w = int(input('몇 개 마다 줄 바꿈?'))

for i in range(n):
    print(f"{i}*",end="")
    if i%w==w-1:
        print()
        
if n%w:
    print()        