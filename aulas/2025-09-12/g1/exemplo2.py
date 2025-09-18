def calcular_media_aritmetica(nota1: int, nota2: int, nota3: int) -> float:
    return (nota1 + nota2 + nota3) / 3

def calcular_media_ponderada(nota1: int, nota2: int, nota3: int) -> float:
    return (nota1 * 3 + nota2 * 4 + nota3 * 5) / 12

def calcular_media_final(media1: float, media2: float) -> float:
    if (media1 > media2):
        return media1
    else:
        return media2

def verificar_situacao(media: float) -> str:
    if media >= 70:
        return 'Aprovado'
    else:
        return 'Reprovado'

# main
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

ma = calcular_media_aritmetica(nota1, nota2, nota2)
mp = calcular_media_ponderada(nota1, nota2, nota3)

media = calcular_media_final(ma, mp)

situacao = verificar_situacao(media)

print(ma, mp, media, situacao)
