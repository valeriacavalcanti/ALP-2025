hora_inicio, hora_fim = input().split()
hora_inicio, hora_fim = int(hora_inicio), int(hora_fim)

if (hora_inicio < hora_fim):
  # começou e terminou no mesmo dia
  tempo = hora_fim - hora_inicio
else:
  # começou em um dia e terminou no outro
  tempo = 24 - hora_inicio + hora_fim

print("O JOGO DUROU {} HORA(S)".format(tempo))