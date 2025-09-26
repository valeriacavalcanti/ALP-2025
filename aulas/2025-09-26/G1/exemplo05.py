# Programa para ler do usuário 04 números inteiros
# Calcular e exibir a soma desses números

soma = 0

for i in range(4):
    numero = int(input(f'Informe {i+1}º número: '))
    soma = soma + numero

print(i, numero, soma)
