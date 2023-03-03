from reverse import reverse

x=['Jhon','Cena','Paul','Kain']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
reverse(x)
print(x)