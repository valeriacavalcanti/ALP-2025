def menor_valor(valor1: float, valor2: float, valor3: float) -> float:
    if valor1 < valor2 and valor1 < valor3:
        return valor1
    else:
        # valor1 NAO é o menor
        if valor2 < valor3:
            return valor2
        else:
            return valor3


def maior_valor(valor1: float, valor2: float, valor3: float) -> float:
    if valor1 > valor2 and valor1 > valor3:
        return valor1
    else:
        # valor1 NAO é o maior
        if valor2 > valor3:
            return valor2
        else:
            return valor3


def calcular_media(valor1: float, valor2: float, valor3: float) -> float:
    media = (valor1 + valor2 + valor3) / 3
    return media

def exibir(barato: float, caro: float, media: float):
    print(f'Valor mais barato: R$ {barato:.2f}')
    print(f'Valor mais caro: R$ {caro:.2f}')
    print(f'Média dos valores: R$ {media:.2f}')
    

# programa principal

valor_loja_1 = float(input('Informe o valor na loja 1: '))
valor_loja_2 = float(input('Informe o valor na loja 2: '))
valor_loja_3 = float(input('Informe o valor na loja 3: '))

mais_barato = menor_valor(valor_loja_1, valor_loja_2, valor_loja_3)
mais_caro = maior_valor(valor_loja_1, valor_loja_2, valor_loja_3)
media_lojas = calcular_media(valor_loja_1, valor_loja_2, valor_loja_3)

exibir(mais_barato, mais_caro, media_lojas)



