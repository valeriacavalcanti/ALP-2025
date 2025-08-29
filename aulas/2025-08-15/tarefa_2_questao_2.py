valor_compra = float(input('Valor da compra: '))

desconto = valor_compra * 0.1
juros = valor_compra * 0.1

valor_vista = valor_compra - desconto
valor_30_dias = valor_compra
valor_parcelado = valor_compra + juros

print(f'Valor a vista: {valor_vista:.2f}')
print(f'Valor p 30 dias: {valor_30_dias:.2f}')
print(f'Valor parcelado: {valor_parcelado:.2f}')
