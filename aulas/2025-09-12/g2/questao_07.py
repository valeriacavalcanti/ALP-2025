nota = int(input('Nota: '))

if nota >= 90:
    print('A')
else:
    if nota >= 80:
        print('B')
    else:
        if nota >= 70:
            print('C')
        else:
            if nota >= 60:
                print('D')
            else:
                print('F')
