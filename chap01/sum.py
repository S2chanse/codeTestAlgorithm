print(1)

a = int(input('input a : '))
b = int(input('input b : '))
sum = 0
if b<a: 
   a,b = b,a
for i in range(a,b+1):
    sum+=i
print(sum)
