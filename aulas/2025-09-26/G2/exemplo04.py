# programa para ler 3 números
# calcular e exibir a soma desses números lidos
# Calcular e exibir a quantidade de números positivos (>0)

soma = 0
quantidade = 0

for i in range(3):
    num = int(input('Número: '))
    soma = soma + num

    if num > 0:
        quantidade = quantidade + 1
        

print(soma)
print(quantidade)
