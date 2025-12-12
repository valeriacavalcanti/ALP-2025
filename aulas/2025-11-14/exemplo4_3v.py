'''
Programa para ler 6 (seis) valores inteiros e exibir
quais valores são maiores do que o último valor lido.
'''

numeros = []
maiores = []

# ler os valores e armazenar na lista
for i in range(6):
    num = int(input('Número: '))
    numeros.append(num)

ultimo_valor = numeros[len(numeros) - 1]

# comparar todos os valores com o último digitado
for i in range(len(numeros)):
    if numeros[i] > ultimo_valor:
        maiores.append(numeros[i])

print(maiores)




    
    
