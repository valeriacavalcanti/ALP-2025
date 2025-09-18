nome1 = input('Nome 1: ')
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
tempo1 = hora * 3600 + minuto * 60 + segundo

nome2 = input('Nome 2: ')
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
tempo2 = hora * 3600 + minuto * 60 + segundo

if tempo1 < tempo2:
    print(nome1)
else:
    print(nome2)
