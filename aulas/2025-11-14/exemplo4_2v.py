'''
Programa para ler 6 (seis) valores inteiros e exibir
quais valores são maiores do que o último valor lido.
'''

numeros = []

# ler os valores e armazenar na lista
for i in range(6):
    num = int(input('Número: '))
    numeros.append(num)
    # numeros.append(int(input('Número: ')))

#ultimo_valor = numeros[5]
ultimo_valor = numeros[len(numeros) - 1]

# comparar todos os valores com o último digitado
for i in range(len(numeros)):
    if numeros[i] > ultimo_valor:
        print(i, numeros[i])




    
    
