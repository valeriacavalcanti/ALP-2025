nota1 = input('Digite nota 1: ')
nota1 = float(nota1)

nota2 = float(input('Digite nota 2: '))
nota3 = float(input('Digite nota 3: '))
nota4 = float(input('Digite nota 4: '))

ma = (nota1 + nota2 + nota3 + nota4) / 4
mp = (nota1*2 + nota2*3 + nota3*3 + nota4*6)/14

print('Média aritmética',ma)
print('Média ponderada:', mp)
print(f'Média ponderada: {mp:.2f}')
print(f'Média ponderada: {mp:10.2f}')

