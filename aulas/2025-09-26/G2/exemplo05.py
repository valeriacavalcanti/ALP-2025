# programa para ler 3 números
# calcular e exibir a soma dos números positivos

soma = 0

for i in range(3):
    #print(i + 1)
    num = int(input(f'Número {i+1}: '))
    
    if num > 0:
        soma = soma + num
        
print(soma)
