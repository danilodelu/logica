def calcular_folha():
    try:
        salario_bruto = float(input("Digite o valor do salário bruto (R$): "))

        # 1. Cálculo do INSS (Tabela simplificada 2023)
        if salario_bruto <= 1302.00:
            inss = salario_bruto * 0.075
        elif salario_bruto <= 2571.29:
            inss = salario_bruto * 0.09
        elif salario_bruto <= 3856.94:
            inss = salario_bruto * 0.12
        else:
            inss = salario_bruto * 0.14
        
        # O teto do INSS em 2023 era aproximadamente R$ 877,24
        if inss > 877.24:
            inss = 877.24

        # 2. Base de cálculo para o IRRF
        base_irrf = salario_bruto - inss

        # 3. Cálculo do IRRF (Tabela 2023)
        if base_irrf <= 1903.98:
            irrf = 0.0
        elif base_irrf <= 2826.65:
            irrf = (base_irrf * 0.075) - 142.80
        elif base_irrf <= 3751.05:
            irrf = (base_irrf * 0.15) - 354.80
        elif base_irrf <= 4664.68:
            irrf = (base_irrf * 0.225) - 636.13
        else:
            irrf = (base_irrf * 0.275) - 869.36

        salario_liquido = salario_bruto - inss - irrf

        # Exibição dos Resultados
        print("-" * 35)
        print(f"Salário Bruto:   R$ {salario_bruto:>8.2f}")
        print(f"Desconto INSS:   R$ {inss:>8.2f}")
        print(f"Desconto IRRF:   R$ {irrf:>8.2f}")
        print("-" * 35)
        print(f"Salário Líquido: R$ {salario_liquido:>8.2f}")
        print("-" * 35)

    except ValueError:
        print("Erro: Digite um valor numérico válido.")

calcular_folha()