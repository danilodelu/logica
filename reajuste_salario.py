# Entrada de dados
try:
    salario_atual = float(input("Digite o salário atual do funcionário (R$): "))

    # Lógica para determinar o percentual de aumento
    if salario_atual <= 1000.00:
        percentual = 20
    elif salario_atual <= 1700.00:
        percentual = 15
    elif salario_atual <= 2300.00:
        percentual = 10
    else:
        percentual = 5

    # Cálculos
    valor_aumento = salario_atual * (percentual / 100)
    novo_salario = salario_atual + valor_aumento

    # Exibição dos resultados detalhados
    print("-" * 35)
    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento:    {percentual}%")
    print(f"Valor do aumento:         R$ {valor_aumento:.2f}")
    print("-" * 35)
    print(f"Novo salário:             R$ {novo_salario:.2f}")
    print("-" * 35)

except ValueError:
    print("Erro: Por favor, insira um valor numérico válido para o salário.")
