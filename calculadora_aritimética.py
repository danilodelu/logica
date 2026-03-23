import math

# Entrada dos números
try:
    num1 = float(input("Digite o primeiro número: "))
    # A raiz quadrada e o teste de par/ímpar geralmente focam no primeiro número, 
    # mas para as outras operações precisaremos do segundo:
    num2 = float(input("Digite o segundo número: "))

    print("\n--- CALCULADORA ---")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência (n1 elevado a n2)")
    print("6 - Raiz quadrada (de n1)")
    print("7 - Verificar se n1 é Par")
    print("8 - Verificar se n1 é Ímpar")
    
    opcao = input("\nEscolha uma operação (1-8): ")

    if opcao == "1":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcao == "2":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcao == "3":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não permitida.")
    elif opcao == "5":
        resultado = num1 ** num2
        print(f"Resultado: {num1} elevado a {num2} = {resultado}")
    elif opcao == "6":
        if num1 >= 0:
            resultado = math.sqrt(num1)
            print(f"A raiz quadrada de {num1} é {resultado:.2f}")
        else:
            print("Erro: Não existe raiz quadrada de número negativo nos Reais.")
    elif opcao == "7":
        if num1 % 2 == 0:
            print(f"O número {num1} é PAR.")
        else:
            print(f"O número {num1} NÃO é par.")
    elif opcao == "8":
        if num1 % 2 != 0:
            print(f"O número {num1} é ÍMPAR.")
        else:
            print(f"O número {num1} NÃO é ímpar.")
    else:
        print("Opção inválida!")

except ValueError:
    print("Erro: Digite apenas valores numéricos.")

print("\nFim do programa!")