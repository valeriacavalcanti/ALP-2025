distintos = []

while len(distintos) != 4:
    num = int(input('Número: '))

    if num not in distintos:
        distintos.append(num)

print(distintos)
