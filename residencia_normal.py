# Entrada de dados
consumo = float(input("Digite o consumo de água em m³: "))

# Lógica de cálculo baseada nas faixas
if consumo <= 10:
    valor_conta = 22.38
elif consumo <= 20:
    valor_conta = consumo * 3.50
elif consumo <= 50:
    valor_conta = consumo * 8.75
else:
    valor_conta = consumo * 9.64

# Exibição do resultado formatado
print(f"O valor da conta de água é: R$ {valor_conta:.2f}")