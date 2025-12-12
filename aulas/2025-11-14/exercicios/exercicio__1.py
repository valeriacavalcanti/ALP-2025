import random

numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input('Número: '))

valor_aleatorio = random.randint(1, 20)

existe = False
for i in range(10):
    if numeros[i] == valor_aleatorio:
        existe = True
        break

if existe == True:
    print('tem')
else:
    print('nao tem')

print(numeros)
print(valor_aleatorio)
