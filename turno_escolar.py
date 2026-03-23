# Entrada de dados
print("Informe o turno em que você estuda:")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")

turno = input("Digite a letra correspondente: ")

# Estrutura de decisão (verificação rigorosa de maiúsculas)
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

print("Fim do processamento.")