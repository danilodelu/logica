# Entrada de dados para os três lados
try:
    lado1 = float(input("Digite o valor do primeiro lado (A): "))
    lado2 = float(input("Digite o valor do segundo lado (B): "))
    lado3 = float(input("Digite o valor do terceiro lado (C): "))

    # 1. Verificação da existência do triângulo
    # A soma de dois lados deve ser sempre MAIOR que o terceiro
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        
        print("\nOs valores informados FORMAM um triângulo.")

        # 2. Classificação do tipo de triângulo
        if lado1 == lado2 == lado3:
            tipo = "Equilátero (todos os lados iguais)"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            tipo = "Isósceles (dois ou mais lados iguais)"
        else:
            tipo = "Escaleno (todos os lados diferentes)"

        print(f"Tipo: {tipo}")

    else:
        print("\nOs valores informados NÃO podem formar um triângulo.")
        print("Motivo: A soma de dois lados não é maior que o terceiro.")

except ValueError:
    print("Erro: Por favor, digite apenas números.")