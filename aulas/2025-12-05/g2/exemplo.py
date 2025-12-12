import random

qtd = 0

# declarar vetor de tamanho 30
numeros = [0] * 30

# preencher o vetor com valores aleatórios (entre 1 e 10)
for i in range(30):
    numeros[i] = random.randint(1, 1000)

# exibir os números gerados
print(numeros)

# ler um valor do usuário
valor = int(input('Digite um valor: '))

# calcular quantas vezes esse número lido aparece no vetor
for i in range(30):
    if valor == numeros[i]:
        qtd = qtd + 1

# Exibir a frequência calculada
print(f'{qtd=}')

# verificar se tem repetição

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
    print('Tem repetição')
else:
    print('Não tem repetição')
    
