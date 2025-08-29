a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

# descobrir qual é o maior lado
if a > b and a > c:
    maior = a
    soma = b + c
else:
    if b > c:
        maior = b
        soma = a + c
    else:
        maior = c
        soma = a + b

print(nome)

# verificar se forma triangulo
if maior < soma:
    perimetro = a + b + c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((a + b) * c) / 2
    print(f'Area = {area:.1f}')


