# programa para ler 3 números
# calcular e exibir a soma desses números lidos

soma = 0

for i in range(3):
    num = int(input('Número: '))
    soma = soma + num

print(soma)
