numeros = [0] * 4

for i in range(4):
    numeros[i] = int(input('Número: '))

tem_repeticao = False
for i in range(4):
    if numeros.count(numeros[i]) > 1:
        tem_repeticao = True
        break

if tem_repeticao == True:
    print('Tem repetição')
else:
    print('Não tem repetição')
