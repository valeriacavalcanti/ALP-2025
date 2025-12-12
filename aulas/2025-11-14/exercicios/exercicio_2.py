import random

qtd = 0
numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input('Número: '))

valor_aleatorio = random.randint(1, 10)

'''
for i in range(10):
    if numeros[i] == valor_aleatorio:
        qtd = qtd + 1
'''
qtd = numeros.count(valor_aleatorio)

print(f'{numeros = }')
print(f'{valor_aleatorio = }')
print(f'{qtd = }')
