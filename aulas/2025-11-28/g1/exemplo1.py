# declarar um vetor de tamanho 6
numeros = [0] * 6

# ler 6 números e armazenar no vetor
for i in range(len(numeros)):
    numeros[i] = int(input('Número: '))

# exibir todos os valores que estão no vetor
for i in range(len(numeros)):
    print(numeros[i])

# somar todos os elementos que estão no vetor
soma = 0
for i in range(len(numeros)):
    soma = soma + numeros[i]

# calcular a média dos valores armazenados no vetor
media = soma / len(numeros)

# calcular a quantidade de elementos armazenados no vetor com valor
# acima da média
qtd = 0
for i in range(len(numeros)):
    if numeros[i] > media:
        qtd = qtd + 1

# exibir a soma, a média e a quantidade acima da média
print(soma, media, qtd)
