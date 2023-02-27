# 구구단
print('-' * 27)

for i in range(1,10):
    for j in range(1,10):
        print(f'{j:2} x {i:2} = {i*j:3}',end = ' ')
    print()
print('-' * 27)    