n = int(input())
for _ in range(n):
    m = int(input())
    array = []  
    for i in range(2,m+1):
        #소수리스트를 구한다.
        for j in range(2,i+1):
            if i%j == 0:
                if j == i:
                    array.append(i)
                break
    for                 
                    