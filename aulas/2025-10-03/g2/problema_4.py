def nota_valida(nota: int) -> bool:
    if nota >= 0 and nota <= 100:
        return True
    else:
        return False


## Programa principal
quantidade_notas_validas = 0

for i in range(6):
    nota_aluno = int(input('Nota: '))
    # validar
    if nota_valida(nota_aluno) == True:
        quantidade_notas_validas = quantidade_notas_validas + 1

print(quantidade_notas_validas, 'notas válidas')
