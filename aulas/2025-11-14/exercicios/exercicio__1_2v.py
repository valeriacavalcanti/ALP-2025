import random

numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input('Número: '))

valor_aleatorio = random.randint(1, 20)

if valor_aleatorio in numeros:
    print('tem')
else:
    print('nao tem')

print(numeros)
print(valor_aleatorio)
