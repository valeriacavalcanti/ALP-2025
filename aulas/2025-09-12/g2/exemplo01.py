def calcular_quociente(dividendo: int, divisor: int) -> int:
    resultado = dividendo // divisor
    return resultado

    
def calcular_resto(dividendo: int, divisor: int) -> int:
    return dividendo % divisor


# principal

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

quociente = calcular_quociente(num1, num2)
resto = calcular_resto(num1, num2)

print(num1, num2, quociente, resto)
