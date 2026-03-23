# Entrada do número do dia
try:
    dia_num = int(input("Digite um número de 1 a 7 para o dia da semana: "))

    # Estrutura condicional para verificar o dia
    if dia_num == 1:
        print("1 - Domingo")
    elif dia_num == 2:
        print("2 - Segunda-feira")
    elif dia_num == 3:
        print("3 - Terça-feira")
    elif dia_num == 4:
        print("4 - Quarta-feira")
    elif dia_num == 5:
        print("5 - Quinta-feira")
    elif dia_num == 6:
        print("6 - Sexta-feira")
    elif dia_num == 7:
        print("7 - Sábado")
    else:
        # Caso o número não esteja entre 1 e 7
        print("Erro: Número inválido! Por favor, digite um valor entre 1 e 7.")

except ValueError:
    print("Erro: Entrada inválida! Digite apenas números inteiros.")