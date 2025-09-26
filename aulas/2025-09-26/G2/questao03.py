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


# programa principal

print(menor_valor(10,20,30))
print(menor_valor(30,20,30))

