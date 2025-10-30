def nota_valida(nota: int) -> bool:
    if (nota >= 0) and (nota <= 100):
        return True
    else:
        return False


# Programa Principal

qtd_notas_validas = 0

for i in range(6):
    nota_aluno = int(input('Nota: '))
    if nota_valida(nota_aluno) == True:
        qtd_notas_validas = qtd_notas_validas + 1

print(f'Quantidade = {qtd_notas_validas}')
