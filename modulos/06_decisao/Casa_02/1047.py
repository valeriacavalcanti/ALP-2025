hora_inicio, minuto_inicio, hora_fim, minuto_fim = input().split()
hora_inicio, minuto_inicio, hora_fim, minuto_fim = int(hora_inicio), int(minuto_inicio), int(hora_fim), int(minuto_fim)

inicio = hora_inicio * 60 + minuto_inicio
fim = hora_fim * 60 + minuto_fim

if (inicio == fim):
  print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
  if (inicio < fim):
    hora = (fim - inicio) // 60
    minuto = (fim - inicio) % 60
  else:
    hora = ((24 * 60 - inicio) + fim) // 60
    minuto = ((24 * 60 - inicio) + fim) % 60
  print('O JOGO DUROU {:d} HORA(S) E {:d} MINUTO(S)'.format(hora, minuto))