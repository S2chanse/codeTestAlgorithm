n = int(input())
arr = [None]*n
max = 0
maxIdx = 0
for i in range(n):
    arr[i] = int(input())
    
arr.sort()

for i in arr:
    print(i)


