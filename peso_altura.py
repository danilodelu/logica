# Entrada de dados
try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    # Cálculo do IMC
    # Usamos altura ** 2 para elevar ao quadrado
    imc = peso / (altura ** 2)

    # Lógica de classificação
    if imc < 16:
        status = "Magreza grave"
    elif imc < 17:
        status = "Magreza moderada"
    elif imc < 18.5:
        status = "Magreza leve"
    elif imc < 25:
        status = "Saudável"
    elif imc < 30:
        status = "Sobrepeso"
    elif imc < 35:
        status = "Obesidade Grau I"
    elif imc < 40:
        status = "Obesidade Grau II (severa)"
    else:
        status = "Obesidade Grau III (mórbida)"

    # Exibição dos resultados
    print("-" * 30)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {status}")
    print("-" * 30)

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")