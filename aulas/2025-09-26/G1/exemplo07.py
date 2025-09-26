# Programa para ler do usuário 04 números inteiros
# Calcular e exibir a soma dos números positivos

soma = 0

for i in range(4):
    numero = int(input(f'Informe {i+1}º número: '))
    
    if numero > 0:
        soma = soma + numero

print(i, numero, soma)
