def converte_celcius(tf: float) -> float:
    return (5 * (tf - 32)) / 9

def avaliar_fervendo(tf: float) -> bool:
    tc = converte_celcius(tf)
    if tc >= 100:
        return True
    else:
        return False


## Programa Principal

temperatura = float(input('Temperatura Fahrenheit: '))

if (avaliar_fervendo(temperatura) == True):
    print('Está fervendo')
else:
    print('Não está fervendo')
