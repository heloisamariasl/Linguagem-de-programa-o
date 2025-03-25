#13
salario_inicial = float(input("Digite o salário inicial:"))
anos = int(input("Digite a quantidade de anos:"))
salario_atual = salario_inicial
aumento_percentual = 1  
for ano in range(1, anos + 1):
    salario_atual += salario_atual * (aumento_percentual / 100)
    aumento_percentual *= 2  
print(f"O salário atual após {anos} foi é R${salario_atual} (:")
