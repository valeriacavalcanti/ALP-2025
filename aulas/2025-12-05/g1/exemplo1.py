import random

qtd = 0

# declarar um vetor de 30 elementos
numeros = [0] * 30

# preencher o vetor com valores aleatórios (entre 1 e 10)
for i in range(30):
    numeros[i] = random.randint(1, 10)

# exibir o vetor
print(numeros)

# ler um valor do usuário
valor = int(input('Digite um valor: '))

# calcular a quantidade de vezes que o número aparece no vetor
for i in range(30):
    if valor == numeros[i]:
        qtd = qtd + 1

# exibir a quantidade calculada
print(f'{qtd=}')

# verificar se tem repeticao!
existe_repeticao = False
for i in range(30):
    qtd = 0
    for j in range(30):
        if numeros[i] == numeros[j]:
            qtd = qtd + 1
    if qtd > 1:
        existe_repeticao = True
        break

if existe_repeticao == True:
    print('Existe repetição')
else:
    print('Não existe repetição')
