numeros = [0] * 6
soma = 0
qtd_acima = 0

# ler 6 números e armazenar no vetor
for i in range(len(numeros)):
    numeros[i] = int(input('Número: '))

# somar todos os elementos que estão armazenados no vetor
for i in range(len(numeros)):
    soma = soma + numeros[i]

media = soma / len(numeros)

# calcular a quantidade de elementos que estão armazenados no vetor
# que possuem valor acima da média calculada
for i in range(len(numeros)):
    if numeros[i] > media:
        qtd_acima = qtd_acima + 1

print(f'{qtd_acima=}')
print(f'{media=}')
