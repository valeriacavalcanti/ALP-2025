soma = 0
qtd_numeros_digitados = 0

while True:
    numero = int(input('Número: '))

    if numero == 0:
        break

    soma = soma + numero
    qtd_numeros_digitados = qtd_numeros_digitados + 1


# saiu do while

if qtd_numeros_digitados > 0:
    media = soma / qtd_numeros_digitados

    print(f'Soma = {soma}')
    print(f'Quantidade = {qtd_numeros_digitados}')
    print(f'Média = {media}')
else:
    print('Nenhum número digitado')
