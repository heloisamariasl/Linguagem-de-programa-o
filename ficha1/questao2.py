#2 
tempo = int(input("Digite o tempo em segundos:"))
dias = tempo // 86400
tempo_restante = tempo % 86400

horas = tempo_restante // 3600
tempo_restante  = tempo_restante  % 3600

minutos = tempo_restante  // 60
tempo_restante  = tempo_restante  % 60

print(f"São {dias} dias, {horas} horas, {minutos} minutos e {tempo_restante } segundos")
