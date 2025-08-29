valor_compra = float(input('Informe o valor da compra: '))

desconto = valor_compra * 0.1
pagamento_a_vista = valor_compra - desconto

acrescimo = valor_compra * 0.1
parcelado = valor_compra + acrescimo

print(f'À vista: {pagamento_a_vista}')
print(f'30 dias: {valor_compra}')
print(f'Parcelado: {parcelado}')