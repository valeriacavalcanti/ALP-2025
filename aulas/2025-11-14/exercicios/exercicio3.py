numeros_pares = []

# ler os valores
for i in range(10):
    num = int(input('Número: '))
    if num % 2 == 0:
        numeros_pares.append(num)

# exibir os números pares
print(numeros_pares)

for i in range(len(numeros_pares)):
    print(numeros_pares[i])
