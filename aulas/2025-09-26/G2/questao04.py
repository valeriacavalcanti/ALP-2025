def menor_valor(valor1:float, valor2:float, valor3:float) -> float:
    if valor1 < valor2 and valor1 < valor3:
        return valor1
    else:
        # valor1 NAO é o menor
        if valor2 < valor3:
            return valor2
        else:
            return valor3


def maior_valor(valor1:float, valor2:float, valor3:float) -> float:
    if valor1 > valor2 and valor1 > valor3:
        return valor1
    else:
        # valor1 NAO é o maior
        if valor2 > valor3:
            return valor2
        else:
            return valor3


def calcular_media(valor1:float, valor2:float, valor3:float) -> float:
    return (valor1 + valor2 + valor3)/3


def exibir(barato: float, caro: float, media: float):
    print(f'Mais barato: R$ {barato:.2f}')
    print(f'Mais caro: R$ {caro:.2f}')
    print(f'Média: R$ {media:.2f}')

# programa principal

descricao = input('Descrição: ')
valor_loja_1 = float(input('Primeiro preço: '))
valor_loja_2 = float(input('Segundo preço: '))
valor_loja_3 = float(input('Terceiro preço: '))

barato = menor_valor(valor_loja_1, valor_loja_2, valor_loja_3)
caro = maior_valor(valor_loja_1, valor_loja_2, valor_loja_3)
media = calcular_media(valor_loja_1, valor_loja_2, valor_loja_3)

exibir(barato, caro, media)
