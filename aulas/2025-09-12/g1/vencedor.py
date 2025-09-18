def Converter_para_segundos(hora:int, minuto:int, segundo:int) -> int:
    return (hora * 3600) + (minuto * 60) + segundo


def Verificar_vencedor(nome1:str, tempo1:int, nome2:str, tempo2:int) -> str:
    if tempo1 < tempo2:
        return nome1
    else:
        return nome2

# main

nome1 = input('Nome 1: ')
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))

tempo1 = Converter_para_segundos(hora, minuto, segundo)

nome2 = input('Nome 2: ')
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))

tempo2 = Converter_para_segundos(hora, minuto, segundo)

vencedor = Verificar_vencedor(nome1, tempo1, nome2, tempo2)

print(vencedor)
