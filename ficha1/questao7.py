#7
numero = int(input("Digite um número ímpar:"))
if numero % 2 != 0:
    anterior = numero - 2
    proximo = numero + 2
    diferenca = (proximo ** 2) - (anterior ** 2)
    print("A diferença entre o quadrado do próximo número ímpar e do anterior é:", diferenca)
else:
    print("Digite um número ímpar.")
