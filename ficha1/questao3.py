#3
valor = int(input("Digite o valor de mercadorias compradas: "))
if valor <= 500:
    print("Sem imposto :)")
else:
    imposto = (valor - 500) * 0.5
    print(f"O imposto a ser pago é de R$ {imposto} ")
