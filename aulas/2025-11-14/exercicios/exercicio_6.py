distintos = []

while True:
    num = int(input('Número: '))

    if num not in distintos:
        distintos.append(num)

    if len(distintos) == 4:
        break

print(distintos)
