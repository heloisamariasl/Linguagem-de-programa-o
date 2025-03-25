#4
dias = int(input("Por quantos dias andou com o carro?"))
km = int(input("Por quantos Km?"))
if km > 100:
    x = km - 100 
    taxa=  x * 12 
else:
    taxa = 0

valor = dias*90 + taxa
print("Valor:", valor)
