#12
turmas = int(input("Digite a quantidade de turmas:"))
alunos_totais = int(input("Digite a quantidade total de alunos:"))

media = alunos_totais / turmas

print(f"A média de alunos por turma é", media)

if media > 40:
    print("Aviso: Alguma turma tem mais de 40 alunos.")
