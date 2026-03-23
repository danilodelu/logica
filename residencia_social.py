#Vamos solicitar o consumo de água em m3
consumo = float(input("Digite o consumo de água em m3: "))

if consumo <= 10:
    valor = 7.59
elif consumo <= 20:
    valor = consumo * 1.31
elif consumo <= 30:
    valor = consumo * 4.64
elif consumo <= 50:
    valor = consumo * 6.62
else:
    valor = consumo * 7.31


    print("Valor da conta = R$ {valor:.2f}")