def converte_para_celcius(tf: float) -> float:
    return (5*(tf-32))/9


def avaliar_fervendo(fahrenheit: float) -> bool:
    tc = converte_para_celcius(fahrenheit)
    if tc >= 100:
        return True
    else:
        return False


# Programa principal

tf = float(input('Temperatura na escala Fahrenheit: '))
if (avaliar_fervendo(tf) == True):
    print('ferve')
else:
    print('nao ferve')
