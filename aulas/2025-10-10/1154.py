soma = 0
qtde = 0
while (True):
    try:
        idade = int(input())
        if (idade < 0):
            break
        soma += idade
        qtde += 1
    except EOFError:
        break

media = soma/qtde
print('{:.2f}'.format(media))