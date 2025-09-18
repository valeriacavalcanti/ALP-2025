def converter_nota_conceito_1(nota:int) -> str:
    if nota < 60:
        return 'F'
    else:
        if nota < 70:
            return 'D'
        else:
            if nota < 80:
                return 'C'
            else:
                if nota < 90:
                    return 'B'
                else:
                    return 'A'


def converter_nota_conceito_2(nota:int) -> str:
    if nota < 60:
        return 'F'
    elif nota < 70:
        return 'D'
    elif nota < 80:
        return 'C'
    elif nota < 90:
        return 'B'
    else:
        return 'A'

# main
nota = int(input('Nota: '))

conceito = converter_nota_conceito_1(nota)

print(converter_nota_conceito_2(nota))

print(conceito)
