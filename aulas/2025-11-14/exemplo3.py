'''
Programa para ler VÁRIOS números inteiros. O programa
deverá encerrar quando for informado 0 (zero).

Ao final exiba TODOS os valores digitados.
'''

numeros = []
while True:
    num = int(input('Número: '))
    if num == 0:
        break
    numeros.append(num)

print(numeros)
