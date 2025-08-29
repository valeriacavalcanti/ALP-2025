#codigo = int(input())
#quantidade = int(input())

codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

# descobrir o valor
if codigo == 1:
    valor = 4
elif codigo == 2:
    valor = 4.5
elif codigo == 3:
    valor = 5
elif codigo == 4:
    valor = 2
else: # código 5
    valor = 1.5 

# calcular o total
total = valor * quantidade

print(f'Total: R$ {total:.2f}')
