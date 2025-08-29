#codigo = int(input())
#quantidade = int(input())

codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

# descobrir o valor do produto
if codigo == 1:
    valor = 4
else: 
    if codigo == 2:
        valor = 4.5
    else:
        if codigo == 3:
            valor = 5
        else:
            if codigo == 4:
                valor = 2
            else:
                valor = 1.5

# calcular o total devido
total = valor * quantidade

# exibir o resultado
print(f'Total: R$ {total:.2f}')

