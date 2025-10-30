soma = 0
quantidade = 0

while True:
    numero = int(input('Número: '))

    if numero == 0:
        break

    quantidade = quantidade + 1
    soma = soma + numero

print('Terminou ...')

if quantidade > 0:
    media = soma / quantidade

    print('Número:', numero)
    print('Quantidade:', quantidade)
    print('Soma:', soma)
    print('Média:', media)
else:
    print('Nenhum valor digitado')
