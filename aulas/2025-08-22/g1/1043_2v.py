a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

# descobrir qual é o maior lado
if a > b and a > c:
    maior = a
else:
    if b > c:
        maior = b
    else:
        maior = c

# descobrir a soma dos outros lados
soma = (a + b + c) - maior

# verificar se forma triangulo
if maior < soma:
    perimetro = a + b + c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((a + b) * c) / 2
    print(f'Area = {area:.1f}')


