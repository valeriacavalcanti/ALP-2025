tempo = int(input())

hora = tempo // 3600
minuto = (tempo % 3600) // 60
segundo = (tempo % 3600) % 60

print(f'{hora}:{minuto}:{segundo}')
