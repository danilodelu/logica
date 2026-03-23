# Entrada de dados para o consumo comercial/industrial
try:
    consumo = float(input("Digite o consumo de água comercial/industrial (m³): "))

    # Lógica de cálculo conforme as faixas fornecidas
    if consumo <= 10:
        valor_conta = 44.95
    elif consumo <= 20:
        valor_conta = consumo * 8.75
    elif consumo <= 50:
        valor_conta = consumo * 16.76
    else:
        valor_conta = consumo * 17.46

    # Exibição do resultado formatado com 2 casas decimais
    print(f"--- Fatura de Água (Comercial/Industrial) ---")
    print(f"Consumo registrado: {consumo} m³")
    print(f"Valor total a pagar: R$ {valor_conta:.2f}")

except ValueError:
    print("Por favor, digite um número válido para o consumo.")