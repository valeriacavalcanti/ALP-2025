# Programa para ler do usuário 04 números inteiros
# Calcular e exibir a soma desses números
# Quantidade de números positivos (>0)

soma = 0
quantidade = 0

for i in range(4):
    numero = int(input(f'Informe {i+1}º número: '))
    
    if numero > 0:
        quantidade = quantidade + 1
    
    soma = soma + numero

print(i, numero, soma, quantidade)
