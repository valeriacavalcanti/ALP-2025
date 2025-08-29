a, b = input().split()
a = int(a)
b = int(b)

# descobrir o maior valor
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

# verificar se maior é multiplo de menor
if maior % menor == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
